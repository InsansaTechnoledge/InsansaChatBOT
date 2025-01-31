from sentence_transformers import SentenceTransformer
import nltk
from nltk.corpus import wordnet
import json
import numpy as np
from typing import List, Dict, Set

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

class SynonymHandler:
    def __init__(self):
        # Use lighter model for better performance
        self.model = SentenceTransformer('paraphrase-MiniLM-L3-v2')
        self.embedding_cache: Dict[str, np.ndarray] = {}
        self.variation_cache: Dict[str, List[str]] = {}
        
        self.common_patterns = {
            'exam': ['exam', 'examination', 'test', 'assessment'],
            'entrance': ['entrance', 'admission', 'qualifying'],
            'recruitment': ['recruitment', 'selection', 'hiring']
        }
        # Comprehensive exam mappings based on your data
        self.exam_fullforms = {
            # National Level Exams
            'NEET': ['National Eligibility cum Entrance Test', 'medical entrance', 'medical exam', 'medical test', 'doctor entrance'],
            'JEE': ['Joint Entrance Examination', 'engineering entrance', 'iit exam', 'iit jee', 'engineering test'],
            'UPSC': ['Union Public Service Commission', 'civil services exam', 'ias exam', 'civil services', 'upsc examination'],
            'GRE': ['Graduate Record Examination', 'graduate exam', 'foreign education test'],
            
            # Research Organizations
            'BARC': ['Bhabha Atomic Research Centre', 'atomic research', 'nuclear research', 'barc examination'],
            'CSIR': ['Council of Scientific and Industrial Research', 'scientific research exam', 'csir examination'],
            'DRDO': ['Defence Research and Development Organisation', 'defence research', 'defense exam', 'drdo test'],
            
            # Public Sector
            'BEL': ['Bharat Electronics Limited', 'electronics corporation', 'bel recruitment', 'bharat electronics'],
            'BPCL': ['Bharat Petroleum Corporation Limited', 'petroleum corporation', 'oil company exam', 'bpcl test'],
            'IOCL': ['Indian Oil Corporation Limited', 'oil corporation', 'petroleum exam', 'iocl recruitment'],
            'ONGC': ['Oil and Natural Gas Corporation', 'oil and gas', 'petroleum sector', 'ongc test'],
            
            # Transportation
            'DMRC': ['Delhi Metro Rail Corporation', 'metro rail', 'delhi metro exam', 'metro recruitment'],
            'RITES': ['Rail India Technical and Economic Service', 'rail technical', 'railway service exam'],
            
            # Postal & Banking
            'GDS': ['Gramin Dak Sevak', 'postal service', 'post office job', 'postal exam'],
            'IPPB': ['India Post Payments Bank', 'postal bank', 'post bank exam', 'payments bank test'],
            'SBI': ['State Bank of India', 'bank exam', 'banking test', 'bank po', 'bank clerk'],
            
            # Healthcare & Research
            'ICMR': ['Indian Council of Medical Research', 'medical research', 'health research exam'],
            
            # Education & Academic
            'IIFT': ['Indian Institute of Foreign Trade', 'foreign trade', 'trade exam', 'business entrance'],
            'UGC NET': ['University Grants Commission National Eligibility Test', 'net exam', 'teaching eligibility', 'professor exam'],
            'KVPY': ['Kishore Vaigyanik Protsahan Yojana', 'science talent exam', 'research fellowship test'],
            
            # Law Enforcement & Security
            'IPS': ['Indian Police Service', 'police service exam', 'law enforcement test'],
            'RPF': ['Railway Protection Force', 'railway police', 'security force exam'],
            'CAPF': ['Central Armed Police Forces', 'armed forces', 'police force exam'],
            'CISF': ['Central Industrial Security Force', 'industrial security', 'security exam'],
            
            # State Services
            'BPSC': ['Bihar Public Service Commission', 'bihar civil services', 'state services bihar'],
            'GPSC': ['Gujarat Public Service Commission', 'gujarat civil services', 'state services gujarat'],
            'MPSC': ['Maharashtra Public Service Commission', 'maharashtra civil services', 'state services maharashtra'],
            'RPSC': ['Rajasthan Public Service Commission', 'rajasthan civil services', 'state services rajasthan'],
            'TNPSC': ['Tamil Nadu Public Service Commission', 'tamil nadu civil services', 'state services tamil nadu'],
            'UPPSC': ['Uttar Pradesh Public Service Commission', 'up civil services', 'state services up'],
            
            # Defense
            'CDS': ['Combined Defence Services', 'defence services exam', 'military entrance'],
            'NDA': ['National Defence Academy', 'defence academy exam', 'military training entrance'],
            
            # Technical Services
            'IES': ['Indian Engineering Services', 'engineering services exam', 'technical services'],
            'ESE': ['Engineering Services Examination', 'engineering services', 'technical exam'],
            
            # Medical Services
            'CMS': ['Combined Medical Services', 'medical services exam', 'government doctor exam'],
            
            # Statistics & Economics
            'ISS': ['Indian Statistical Service', 'statistics service exam', 'government statistician'],
            'CSO': ['Central Statistical Organisation', 'statistics exam', 'government statistics'],
            
            # Regional Transport
            'MSRTC': ['Maharashtra State Road Transport Corporation', 'maharashtra transport', 'state transport exam'],
            'UPSRTC': ['Uttar Pradesh State Road Transport Corporation', 'up transport', 'state transport exam']
        }

    def get_embedding(self, text: str) -> np.ndarray:
        """Get embedding with caching"""
        if text in self.embedding_cache:
            return self.embedding_cache[text]
        
        embedding = self.model.encode([text])[0]
        self.embedding_cache[text] = embedding
        return embedding

    def generate_variations(self, exam_name: str) -> List[str]:
        """Generate variations with caching"""
        if exam_name in self.variation_cache:
            return self.variation_cache[exam_name]

        variations: Set[str] = set()
        variations.add(exam_name)
        
        # Handle acronyms
        if '.' in exam_name:
            variations.add(exam_name.replace('.', ''))
        if exam_name.isupper() and len(exam_name) > 1:
            variations.add('.'.join(list(exam_name)))
            
        # Add full forms and variations
        if exam_name in self.exam_fullforms:
            variations.update(self.exam_fullforms[exam_name])
            
        # Add common patterns
        base_terms = {exam_name.lower()}
        if exam_name in self.exam_fullforms:
            base_terms.update(term.lower() for term in self.exam_fullforms[exam_name])
            
        for term in base_terms:
            for pattern_list in self.common_patterns.values():
                for pattern in pattern_list:
                    variations.add(f"{term} {pattern}")
                    variations.add(f"{pattern} for {term}")
        
        result = list(variations)
        self.variation_cache[exam_name] = result
        return result

    def calculate_similarity(self, query_embedding: np.ndarray, text: str) -> float:
        """Calculate similarity between query and text"""
        text_embedding = self.get_embedding(text)
        return float(np.dot(query_embedding, text_embedding))

    def calculate_similarities_batch(self, query_embedding: np.ndarray, variations: List[str]) -> np.ndarray:
        """Calculate similarities for multiple variations at once"""
        variation_embeddings = [self.get_embedding(v) for v in variations]
        return np.dot(variation_embeddings, query_embedding)

    def precompute_embeddings(self, variations: List[str]) -> None:
        """Precompute embeddings for all variations"""
        for variation in variations:
            if variation not in self.embedding_cache:
                self.embedding_cache[variation] = self.model.encode([variation])[0]