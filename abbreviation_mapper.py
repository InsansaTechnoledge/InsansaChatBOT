# abbreviation_mapper.py - Contains logic for creating and using abbreviation mappings
import re

def create_abbreviation_mapping(collection):
    """Create a mapping dictionary for abbreviations and their variations"""
    from exam_variations import get_exam_variations
    
    abbreviation_map = {}
    exam_variations = get_exam_variations()
    
    # Get all organizations
    all_organizations = collection.find({})
    
    for org in all_organizations:
        if 'abbreviation' in org and org['abbreviation'] and 'name' in org:
            # Get the original abbreviation and organization name
            abbr = org['abbreviation']
            org_name = org['name']
            
            # Store the org name instead of just the ID to make debugging easier
            # We'll still use the original mapping for lookups
            abbreviation_map[abbr.lower()] = org_name
            
            # Add without spaces
            abbreviation_map[abbr.lower().replace(' ', '')] = org_name
            
            # Add without parentheses
            abbreviation_map[re.sub(r'[\(\)]', '', abbr.lower())] = org_name
            
            # Add without spaces and parentheses
            abbreviation_map[re.sub(r'[\(\)\s]', '', abbr.lower())] = org_name
            
            # Add with different separators
            abbreviation_map[abbr.lower().replace(' ', '-')] = org_name
            abbreviation_map[abbr.lower().replace(' ', '_')] = org_name
            
            # Add specific variations from our database
            if abbr.lower() in exam_variations:
                for var in exam_variations[abbr.lower()]:
                    abbreviation_map[var.lower()] = org_name
    
    return abbreviation_map

def extract_exam_keywords(user_input, abbreviation_map):
    """Extract exact exam keywords from input by checking for known abbreviations"""
    user_input_lower = user_input.lower().strip()
    
    # First check for exact matches in the abbreviation map
    if user_input_lower in abbreviation_map:
        return user_input_lower
    
    # Next check if the input contains any of our abbreviations as a whole word
    # This uses word boundaries \b to prevent partial matches
    for abbr in abbreviation_map.keys():
        # Create a pattern that matches the abbreviation as a whole word
        pattern = r'\b' + re.escape(abbr) + r'\b'
        if re.search(pattern, user_input_lower):
            return abbr
    
    # If no exact match or whole word match found, return original input
    return user_input

def find_organization_by_input(collection, user_input, abbreviation_map):
    """Find an organization based on user input using the mapping"""
    # First try to extract any known exam keyword from the input
    extracted_keyword = extract_exam_keywords(user_input, abbreviation_map)
    
    # If we have an exact match in the abbreviation map
    if extracted_keyword.lower() in abbreviation_map:
        org_name = abbreviation_map[extracted_keyword.lower()]
        # Find by organization name
        return collection.find_one({'name': org_name})
    
    # If not in mapping, try more careful search with exact matching
    user_input_cleaned = extracted_keyword.lower().strip()
    
    # Try exact match by name or abbreviation first
    org = collection.find_one({
        '$or': [
            {'name': {'$regex': f'^{re.escape(user_input_cleaned)}$', '$options': 'i'}},
            {'abbreviation': {'$regex': f'^{re.escape(user_input_cleaned)}$', '$options': 'i'}}
        ]
    })
    
    if org:
        return org
    
    # As a last resort, try to find organizations where the search term is a complete word
    # within the organization name or abbreviation, not a partial match
    word_boundary_pattern = f'\\b{re.escape(user_input_cleaned)}\\b'
    
    return collection.find_one({
        '$or': [
            {'name': {'$regex': word_boundary_pattern, '$options': 'i'}},
            {'abbreviation': {'$regex': word_boundary_pattern, '$options': 'i'}}
        ]
    })