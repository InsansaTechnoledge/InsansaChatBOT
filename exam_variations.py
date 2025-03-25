# exam_variations.py - Contains data about exam name variations

def get_exam_variations():
    """Returns a dictionary mapping exam abbreviations to their variations"""
    variations = {
        'jee mains': [
        'jee main', 'jee-main', 'jee_main', 'jeemain', 'jeemains',
        'joint entrance examination mains', 'joint entrance examination main',
        'joint entrance exam mains', 'joint entrance exam main',
        'jee', 'joint entrance', 'entrance exam', 'engineering entrance',
        'nta jee', 'jee nta', 'jee 2025', 'jee exam', 'jee test',
        'jee paper', 'jee syllabus', 'jee questions', 'jee 2025 paper',
        'jee preparation', 'jee marks', 'jee eligibility', 'jee result',
        'jee coaching', 'jee mock test', 'jee application', 'jee exam date',
        'jee admission', 'jee cut off', 'jee rank'
    ],
    'neet': [
        'neet ug', 'neet-ug', 'neet_ug', 'neetug', 'neet 2025',
        'national eligibility cum entrance test', 'medical entrance exam',
        'nta neet', 'neet nta', 'neet exam', 'neet medical', 'neet entrance',
        'neet test', 'neet paper', 'neet syllabus', 'neet result', 'neet application',
        'neet 2025 exam', 'neet coaching', 'neet marks', 'neet cutoff', 'neet india',
        'neet registration', 'neet eligibility', 'neet question paper',
        'neet biology', 'neet chemistry', 'neet physics', 'neet mock test'
    ],
    'ntse': [
        'ntse exam', 'ntse 2025', 'national talent search exam', 'national talent search examination',
        'ntse scholarship', 'ntse stage 1', 'ntse stage 2', 'ntse paper',
        'ntse test', 'ntse entrance', 'ntse ncert', 'ncert ntse',
        'ntse india', 'ntse question paper', 'ntse eligibility', 'ntse syllabus',
        'ntse 2025 test', 'ntse exam date', 'ntse result', 'ntse application',
        'ntse stage 1 result', 'ntse stage 2 result', 'ntse cut off', 'ntse study material'
    ],
    'npcil': [
        'npcil exam', 'npcil recruitment', 'npcil 2025', 'nuclear power corporation of india',
        'npcil application', 'npcil notification', 'npcil syllabus', 'npcil vacancy',
        'npcil india', 'npcil eligibility', 'npcil details', 'npcil events',
        'npcil 2025 recruitment', 'npcil job openings', 'npcil interview', 'npcil jobs',
        'npcil selection process', 'npcil career', 'npcil result', 'npcil training',
        'npcil admit card', 'npcil test date', 'npcil vacancies 2025'
    ],
    'kvpy': [
        'kvpy exam', 'kvpy 2025', 'kishore vaigyanik protsahan yojana', 'kvpy scholarship',
        'kvpy application', 'kvpy result', 'kvpy eligibility', 'kvpy stage 1', 'kvpy stage 2',
        'kvpy interview', 'kvpy selection process', 'kvpy paper', 'kvpy syllabus',
        'kvpy india', 'kvpy mock test', 'kvpy result 2025', 'kvpy previous year papers',
        'kvpy application form', 'kvpy result date', 'kvpy cut off', 'kvpy guide', 'kvpy coaching'
    ],
    'indian post': [
        'indian post recruitment', 'indian post exam', 'indian post jobs', 'india post application',
        'indian post mail', 'india post details', 'indian post vacancies', 'indian post services',
        'india post delivery', 'indian post notification', 'indian post eligibility',
        'indian post recruitment 2025', 'indian post job openings', 'indian post application form',
        'india post results', 'india post clerk', 'india post postman', 'india post gds',
        'india post mailman', 'indian post application status', 'india post job alert'
    ],
    'ippb': [
        'ippb exam', 'ippb recruitment', 'india post payments bank', 'ippb job openings',
        'ippb application', 'ippb india', 'ippb banking services', 'ippb eligibility',
        'ippb result', 'ippb notification', 'ippb vacancies', 'ippb india 2025',
        'ippb test', 'ippb exam date', 'ippb admit card', 'ippb interview',
        'ippb application form', 'ippb career', 'ippb job details', 'ippb banking jobs'
    ],
    'sbi': [
        'sbi exam', 'sbi recruitment', 'state bank of india', 'sbi career', 'sbi jobs',
        'sbi clerk', 'sbi po', 'sbi notification', 'sbi bank details', 'sbi india',
        'sbi eligibility', 'sbi syllabus', 'sbi result', 'sbi exam date', 'sbi recruitment 2025',
        'sbi application form', 'sbi selection process', 'sbi bank jobs', 'sbi vacancies',
        'sbi career growth', 'sbi mock test', 'sbi po preparation', 'sbi admit card',
        'sbi probationary officer', 'sbi junior associate', 'sbi assistant', 'sbi po 2025'
    ],
    'csir': [
        'csir exam', 'csir recruitment', 'council of scientific and industrial research',
        'csir india', 'csir application', 'csir research', 'csir notification', 'csir eligibility',
        'csir vacancies', 'csir events', 'csir jobs', 'csir r&d', 'csir career',
        'csir scientist exam', 'csir net exam', 'csir csirnet', 'csir net application',
        'csir exam date', 'csir test', 'csir syllabus', 'csir previous year papers'
    ],
    'nda': [
        'nda exam', 'nda 2025', 'national defence academy', 'nda training', 'nda recruitment',
        'nda application', 'nda entrance exam', 'nda eligibility', 'nda syllabus',
        'nda selection process', 'nda interview', 'nda india', 'nda result', 'nda admit card',
        'nda application form', 'nda exam pattern', 'nda written test', 'nda nda 2025',
        'nda exam date', 'nda exam paper', 'nda books', 'nda mock test'
    ],
    'bel': [
        'bel recruitment', 'bel exam', 'bharat electronics limited', 'bel application',
        'bel jobs', 'bel vacancies', 'bel india', 'bel notification', 'bel eligibility',
        'bel event', 'bel career', 'bel r&d', 'bel 2025 recruitment', 'bel interview',
        'bel result', 'bel admit card', 'bel job openings', 'bel salary'
    ],
    'bpcl': [
        'bpcl recruitment', 'bpcl exam', 'bharat petroleum corporation limited',
        'bpcl india', 'bpcl jobs', 'bpcl application', 'bpcl vacancies',
        'bpcl eligibility', 'bpcl notification', 'bpcl career', 'bpcl oil & gas',
        'bpcl selection process', 'bpcl interview', 'bpcl test', 'bpcl results', 
        'bpcl previous year paper', 'bpcl admit card', 'bpcl 2025'
    ],
    'barc': [
        'barc recruitment', 'barc exam', 'bhabha atomic research centre',
        'barc india', 'barc jobs', 'barc application', 'barc vacancies',
        'barc eligibility', 'barc notification', 'barc career', 'barc research',
        'barc scientist exam', 'barc test', 'barc result', 'barc admit card',
        'barc previous year papers', 'barc selection process', 'barc interview'
    ],
    'drdo': [
        'drdo recruitment', 'drdo exam', 'defence research and development organisation',
        'drdo india', 'drdo jobs', 'drdo application', 'drdo vacancies',
        'drdo eligibility', 'drdo notification', 'drdo career', 'drdo defence',
        'drdo scientist exam', 'drdo test', 'drdo result', 'drdo selection process',
        'drdo interview', 'drdo application form', 'drdo previous year papers'
    ],
    'gds': [
        'gds recruitment', 'gds exam', 'gramin dak sevak', 'gds india',
        'gds jobs', 'gds application', 'gds vacancies', 'gds eligibility',
        'gds notification', 'gds postal', 'gds career', 'gds result',
        'gds exam 2025', 'gds previous year paper', 'gds admit card', 'gds test'
    ],
    'icmr': [
        'icmr recruitment', 'icmr exam', 'indian council of medical research',
        'icmr india', 'icmr jobs', 'icmr application', 'icmr vacancies',
        'icmr eligibility', 'icmr notification', 'icmr career', 'icmr research',
        'icmr result', 'icmr exam date', 'icmr selection process', 'icmr application form'
    ],
    'isro': [
        'isro recruitment', 'isro exam', 'indian space research organisation',
        'isro india', 'isro jobs', 'isro application', 'isro vacancies',
        'isro eligibility', 'isro notification', 'isro career', 'isro space research',
        'isro scientist exam', 'isro test', 'isro result', 'isro selection process',
        'isro previous year papers', 'isro admit card'
    ],
    'ongc': [
        'ongc recruitment', 'ongc exam', 'oil and natural gas corporation',
        'ongc india', 'ongc jobs', 'ongc application', 'ongc vacancies',
        'ongc eligibility', 'ongc notification', 'ongc career', 'ongc oil & gas',
        'ongc selection process', 'ongc interview', 'ongc admit card', 'ongc test'
    ],
    'rites': [
        'rites recruitment', 'rites exam', 'rail india technical and economic service',
        'rites india', 'rites jobs', 'rites application', 'rites vacancies',
        'rites eligibility', 'rites notification', 'rites career', 'rites rail',
        'rites result', 'rites selection process', 'rites interview', 'rites admit card'
    ],
    'rpf': [
        'rpf recruitment', 'rpf exam', 'railway protection force',
        'rpf india', 'rpf jobs', 'rpf application', 'rpf vacancies',
        'rpf eligibility', 'rpf notification', 'rpf career', 'rpf railway',
        'rpf test', 'rpf interview', 'rpf selection process', 'rpf admit card'
    ],
    'ntse': [
        'ntse exam', 'ntse 2025', 'national talent search exam',
        'national talent search examination', 'ntse scholarship', 'ntse stage 1',
        'ntse stage 2', 'ntse paper', 'ntse test', 'ntse entrance', 'ntse ncert',
        'ncert ntse', 'ntse india', 'ntse question paper', 'ntse eligibility', 'ntse syllabus'
    ],
    'dmrc': [
        'dmrc recruitment', 'dmrc exam', 'delhi metro rail corporation',
        'dmrc india', 'dmrc jobs', 'dmrc application', 'dmrc vacancies',
        'dmrc eligibility', 'dmrc notification', 'dmrc career', 'dmrc rail'
    ],
    'iocl': [
        'iocl recruitment', 'iocl exam', 'indian oil corporation limited',
        'iocl india', 'iocl jobs', 'iocl application', 'iocl vacancies',
        'iocl eligibility', 'iocl notification', 'iocl career', 'iocl oil & gas'
    ],
    'npcil': [
        'npcil recruitment', 'npcil exam', 'nuclear power corporation of india limited',
        'npcil india', 'npcil jobs', 'npcil application', 'npcil vacancies',
        'npcil eligibility', 'npcil notification', 'npcil career', 'npcil power'
    ],
    'kvpy': [
        'kvpy exam', 'kvpy scholarship', 'kishore vaigyanik protsahan yojana',
        'kvpy india', 'kvpy jobs', 'kvpy application', 'kvpy vacancies',
        'kvpy eligibility', 'kvpy notification', 'kvpy career', 'kvpy research'
    ],
    'ippb': [
        'ippb recruitment', 'ippb exam', 'india post payments bank',
        'ippb india', 'ippb jobs', 'ippb application', 'ippb vacancies',
        'ippb eligibility', 'ippb notification', 'ippb career', 'ippb banking'
    ],
    'sbi': [
        'sbi recruitment', 'sbi exam', 'state bank of india',
        'sbi india', 'sbi jobs', 'sbi application', 'sbi vacancies',
        'sbi eligibility', 'sbi notification', 'sbi career', 'sbi banking'
    ],

    'ssc': [
        'ssc', 'staff selection commission', 'staff selection', 'ssc exam', 'ssc india', 'ssc recruitment', 'ssc jobs',
        'ssc notification', 'ssc syllabus', 'ssc result', 'ssc selection process', 'ssc test', 'ssc admit card'
    ],
    'nabard': [
        'nabard', 'national bank for agriculture and rural development', 'nabard recruitment', 'nabard jobs',
        'nabard notification', 'nabard exam', 'nabard india', 'nabard syllabus', 'nabard eligibility', 'nabard result'
    ],
    'bieap': [
        'bieap', 'board of intermediate education andhra pradesh', 'bieap exam', 'bieap result', 'bieap india',
        'bieap admission', 'bieap syllabus', 'bieap date sheet', 'bieap 2025', 'bieap coaching'
    ],
    'cisf': [
        'cisf', 'central industrial security force', 'cisf exam', 'cisf recruitment', 'cisf jobs', 'cisf india',
        'cisf notification', 'cisf eligibility', 'cisf result', 'cisf admit card', 'cisf test'
    ],
    'upsc': [
        'upsc', 'union public service commission', 'upsc exam', 'upsc recruitment', 'upsc jobs', 'upsc india',
        'upsc notification', 'upsc syllabus', 'upsc eligibility', 'upsc result', 'upsc admit card', 'upsc exam pattern'
    ],
    'apslprb': [
        'apslprb', 'andhra pradesh state level police recruitment board', 'apslprb recruitment', 'apslprb exam',
        'apslprb india', 'apslprb jobs', 'apslprb syllabus', 'apslprb notification', 'apslprb eligibility', 'apslprb result'
    ],
    'capf': [
        'capf', 'central armed police forces', 'capf exam', 'capf recruitment', 'capf assistant commandant',
        'capf notification', 'capf india', 'capf syllabus', 'capf eligibility', 'capf result', 'capf selection process'
    ],
    'bssc': [
        'bssc', 'bihar staff selection commission', 'bssc exam', 'bssc recruitment', 'bssc jobs', 'bssc india',
        'bssc notification', 'bssc syllabus', 'bssc eligibility', 'bssc result', 'bssc admit card'
    ],
    'bpssc': [
        'bpssc', 'bihar police subordinate services commission', 'bpssc exam', 'bpssc recruitment', 'bpssc jobs',
        'bpssc india', 'bpssc notification', 'bpssc syllabus', 'bpssc eligibility', 'bpssc result', 'bpssc admit card'
    ],
    'dmeap': [
        'dmeap', 'directorate of medical education andhra pradesh', 'dmeap india', 'dmeap jobs', 'dmeap recruitment',
        'dmeap notification', 'dmeap eligibility', 'dmeap exam', 'dmeap syllabus', 'dmeap result'
    ],
    'bpsc': [
        'bpsc', 'bihar public service commission', 'bpsc exam', 'bpsc recruitment', 'bpsc jobs', 'bpsc india',
        'bpsc notification', 'bpsc eligibility', 'bpsc result', 'bpsc admit card', 'bpsc exam date'
    ],
    'guvnl': [
        'guvnl', 'gujarat urja vikas nigam limited', 'guvnl recruitment', 'guvnl exam', 'guvnl india', 'guvnl jobs',
        'guvnl notification', 'guvnl eligibility', 'guvnl result', 'guvnl admit card'
    ],
    'hppsc': [
        'hppsc', 'himachal pradesh public service commission', 'hppsc exam', 'hppsc recruitment', 'hppsc jobs',
        'hppsc india', 'hppsc notification', 'hppsc eligibility', 'hppsc result', 'hppsc admit card'
    ],
    'bseb': [
        'bseb', 'bihar school examination board', 'bseb exam', 'bseb result', 'bseb india', 'bseb syllabus',
        'bseb notification', 'bseb eligibility', 'bseb admit card'
    ],
    'bihar energy department': [
        'bihar energy department', 'bihar energy department recruitment', 'bihar energy jobs', 'bihar energy india',
        'bihar energy notification', 'bihar energy exam', 'bihar energy vacancies', 'bihar energy eligibility'
    ],
    'pgvcl': [
        'pgvcl', 'paschim gujarat vij company limited', 'pgvcl recruitment', 'pgvcl exam', 'pgvcl india', 'pgvcl jobs',
        'pgvcl notification', 'pgvcl eligibility', 'pgvcl result', 'pgvcl admit card'
    ],
    'ksp': [
        'ksp', 'karnataka state police', 'ksp recruitment', 'ksp exam', 'ksp india', 'ksp jobs', 'ksp notification',
        'ksp eligibility', 'ksp result', 'ksp admit card'
    ],
    'bceceb': [
        'bceceb', 'bihar combined entrance competitive examination board', 'bceceb exam', 'bceceb recruitment',
        'bceceb india', 'bceceb jobs', 'bceceb notification', 'bceceb eligibility', 'bceceb result'
    ],
    'gsecl': [
        'gsecl', 'gujarat state electricity corporation limited', 'gsecl recruitment', 'gsecl exam', 'gsecl india',
        'gsecl jobs', 'gsecl notification', 'gsecl eligibility', 'gsecl result', 'gsecl admit card'
    ],
    'appsc': [
        'appsc', 'andhra pradesh public service commission', 'appsc recruitment', 'appsc exam', 'appsc india',
        'appsc jobs', 'appsc notification', 'appsc eligibility', 'appsc result', 'appsc admit card'
    ],
    'getco': [
        'getco', 'gujarat energy transmission corporation limited', 'getco recruitment', 'getco exam', 'getco india',
        'getco jobs', 'getco notification', 'getco eligibility', 'getco result', 'getco admit card'
    ],
    'kea': [
        'kea', 'karnataka examinations authority', 'kea recruitment', 'kea exam', 'kea india', 'kea jobs',
        'kea notification', 'kea eligibility', 'kea result', 'kea admit card'
    ],
    'hssc': [
        'hssc', 'haryana staff selection commission', 'hssc recruitment', 'hssc exam', 'hssc india', 'hssc jobs',
        'hssc notification', 'hssc eligibility', 'hssc result', 'hssc admit card'
    ],
    'hte': [
        'hte', 'haryana technical education', 'hte recruitment', 'hte exam', 'hte india', 'hte jobs', 'hte notification',
        'hte eligibility', 'hte result'
    ],
    'btsc': [
        'btsc', 'bihar technical service commission', 'btsc exam', 'btsc recruitment', 'btsc india', 'btsc jobs',
        'btsc notification', 'btsc eligibility', 'btsc result', 'btsc admit card'
    ],

    'hpsc': [
        'hpsc', 'haryana public service commission', 'hpsc exam', 'hpsc recruitment', 'hpsc jobs', 'hpsc india',
        'hpsc notification', 'hpsc eligibility', 'hpsc syllabus', 'hpsc result', 'hpsc admit card', 'hpsc career'
    ],
    'bscb': [
        'bscb', 'bihar state cooperative bank', 'bscb recruitment', 'bscb exam', 'bscb india', 'bscb jobs',
        'bscb notification', 'bscb eligibility', 'bscb result', 'bscb admit card', 'bscb career', 'bscb application'
    ],
    'bseh': [
        'bseh', 'board of school education haryana', 'bseh exam', 'bseh result', 'bseh india', 'bseh notification',
        'bseh syllabus', 'bseh eligibility', 'bseh admit card', 'bseh 2025', 'bseh date sheet', 'bseh board exam'
    ],
    'phed': [
        'phed', 'public health engineering department', 'phed recruitment', 'phed exam', 'phed india', 'phed jobs',
        'phed notification', 'phed eligibility', 'phed result', 'phed admit card', 'phed career', 'phed application'
    ],
    'hppwd': [
        'hppwd', 'himachal pradesh public works department', 'hppwd exam', 'hppwd recruitment', 'hppwd jobs',
        'hppwd india', 'hppwd notification', 'hppwd eligibility', 'hppwd result', 'hppwd admit card', 'hppwd career'
    ],
    'high court of himachal pradesh': [
        'high court of himachal pradesh', 'high court hp', 'himachal pradesh high court', 'hp high court',
        'himachal pradesh high court recruitment', 'high court hp jobs', 'high court hp notification', 
        'high court of himachal pradesh exam', 'high court of himachal pradesh result', 'hp high court admit card'
    ],
    'bank of baroda': [
        'bank of baroda', 'bob', 'bank of baroda recruitment', 'bob exam', 'bank of baroda jobs', 'bank of baroda india',
        'bob india', 'bank of baroda notification', 'bob eligibility', 'bank of baroda application', 'bob result',
        'bob admit card', 'bank of baroda career'
    ],
    'haryana health department': [
        'haryana health department', 'haryana health department recruitment', 'haryana health department jobs',
        'haryana health department exam', 'haryana health department india', 'haryana health department notification',
        'haryana health department eligibility', 'haryana health department result', 'haryana health department admit card',
        'haryana health department career', 'haryana health public health'
    ],
    'mpsc': [
        'mpsc', 'maharashtra public service commission', 'mpsc recruitment', 'mpsc exam', 'mpsc jobs', 'mpsc india',
        'mpsc notification', 'mpsc eligibility', 'mpsc result', 'mpsc admit card', 'mpsc career', 'mpsc application'
    ],
    'high court of kerala': [
        'high court of kerala', 'kerala high court', 'kerala high court recruitment', 'high court kerala jobs',
        'kerala high court notification', 'kerala high court exam', 'high court kerala result', 'kerala high court admit card',
        'high court kerala eligibility', 'kerala high court career'
    ],
    'high court of karnataka': [
        'high court of karnataka', 'karnataka high court', 'karnataka high court recruitment', 'high court karnataka jobs',
        'karnataka high court notification', 'karnataka high court exam', 'high court karnataka result', 
        'karnataka high court admit card', 'high court karnataka eligibility', 'karnataka high court career'
    ],
    'kerala state electricity board': [
        'kerala state electricity board', 'kerala electricity board', 'kseb', 'kerala electricity board recruitment',
        'kseb exam', 'kerala state electricity board jobs', 'kseb india', 'kerala state electricity board notification',
        'kerala state electricity board eligibility', 'kseb admit card', 'kerala state electricity board result',
        'kseb career', 'kseb application'
    ],


    "keralapsc": [
    "keralapsc", "kerala public service commission", "kerala psc", "kerala public service", "kerala recruitment", 
    "kerala jobs", "kerala psc exam", "kerala psc notification", "kerala psc result", "kerala psc admit card", 
    "kerala psc career", "kerala psc eligibility"
    ],
    "maharashtra_zilla_parishad": [
    "maharashtra zilla parishad", "maharashtra zp", "zilla parishad maharashtra", "maharashtra local governing body", 
    "maharashtra parishad", "maharashtra zilla parishad recruitment", "maharashtra zp exam", "maharashtra zilla jobs",
    "maharashtra parishad notification", "maharashtra zp result", "maharashtra zilla parishad admit card"
    ],
    "mppeb": [
    "mppeb", "madhya pradesh professional examination board", "madhya pradesh exam board", "mp professional exam board", 
    "mppeb recruitment", "mppeb exam", "mppeb jobs", "madhya pradesh exam", "mppeb notification", "mppeb result", 
    "mppeb admit card", "mppeb career"
    ],
    "mpsec": [
    "mpsec", "madhya pradesh state election commission", "madhya pradesh election commission", "mp election commission",
    "mpsec recruitment", "mpsec exam", "mpsec jobs", "mpsec result", "mpsec notification", "mpsec admit card", 
    "mpsec career"
    ],
    "mpp": [
    "mpp", "madhya pradesh police", "madhya pradesh police recruitment", "mpp jobs", "madhya pradesh law enforcement", 
    "madhya pradesh police exam", "mpp exam", "mpp result", "mpp notification", "madhya pradesh police admit card", 
    "madhya pradesh police career"
    ],
    "maharashtra_education_board": [
    "maharashtra education board", "maharashtra state board", "maharashtra secondary education board", 
    "maharashtra higher secondary board", "maharashtra board", "maharashtra ssc", "maharashtra hsc", 
    "maharashtra board exam", "maharashtra board result", "maharashtra education recruitment", "maharashtra board jobs"
    ],
    "mppsc": [
    "mppsc", "madhya pradesh public service commission", "madhya pradesh psc", "mppsc recruitment", 
    "mppsc exam", "madhya pradesh psc exam", "mppsc result", "mppsc admit card", "mppsc jobs", "mppsc notification", 
    "mppsc eligibility", "mppsc career"
    ],
    "mprdd": [
    "mprdd", "madhya pradesh rural development department", "madhya pradesh rural development", 
    "madhya pradesh rural development recruitment", "mprdd jobs", "mprdd exam", "mprdd notification", 
    "madhya pradesh rural development result", "mprdd admit card", "mprdd career"
    ],
    "mprdc": [
    "mprdc", "madhya pradesh road development corporation", "madhya pradesh roads", "mprdc development", 
    "mprdc recruitment", "mprdc exam", "mprdc jobs", "madhya pradesh road development", "mprdc result", 
    "mprdc admit card", "mprdc career"
    ],
    "mphc": [
    "mphc", "madhya pradesh high court", "madhya pradesh judiciary", "mp high court", "mphc recruitment", 
    "mphc exam", "madhya pradesh high court jobs", "mphc result", "mphc notification", "mphc admit card", 
    "mphc career"
    ],
    "ossc": [
    "ossc", "odisha staff selection commission", "odisha recruitment", "odisha jobs", "ossc recruitment", 
    "odisha staff recruitment", "odisha exam", "ossc exam", "ossc result", "odisha ossc notification", 
    "ossc admit card", "ossc career"
    ],
    "mpsrtc": [
    "mpsrtc", "madhya pradesh state road transport corporation", "mpsrtc recruitment", "madhya pradesh transport",
    "madhya pradesh roads", "mpsrtc exam", "mpsrtc jobs", "madhya pradesh road transport", "mpsrtc result", 
    "mpsrtc admit card", "mpsrtc career"
    ],
    "odisha_police": [
    "odisha police", "odisha law enforcement", "odisha police recruitment", "odisha police jobs", 
    "odisha police exam", "odisha police result", "odisha police notification", "odisha police admit card", 
    "odisha police career"
    ],
    "mpcd": [
    "mpcd", "madhya pradesh commercial taxes department", "madhya pradesh taxes", "mpcd recruitment", 
    "madhya pradesh commercial taxes exam", "mpcd jobs", "mpcd result", "mpcd admit card", "mpcd career"
    ],
    "osmc": [
    "osmc", "odisha state medical corporation", "odisha medical corporation", "odisha state health services",
    "osmc recruitment", "odisha health department", "osmc exam", "odisha state medical jobs", "osmc result", 
    "osmc admit card", "osmc career"
    ],
    "mpad": [
    "mpad", "madhya pradesh agriculture department", "madhya pradesh agriculture", "mpad recruitment", 
    "mpad exam", "madhya pradesh agricultural jobs", "madhya pradesh farming department", "madhya pradesh crops", 
    "mpad result", "mpad notification", "mpad admit card", "mpad career"
    ],

    "optcl": [
    "optcl", "odisha power transmission corporation limited", "odisha power transmission", "optcl recruitment",
    "optcl exam", "odisha power jobs", "odisha transmission services", "odisha power grid", 
    "optcl result", "optcl notification", "optcl admit card", "optcl career"
    ],
    "high_court_of_orissa": [
    "high court of orissa", "odisha high court", "orissa high court", "odisha judiciary", 
    "odisha high court recruitment", "odisha court jobs", "orissa high court exam", "odisha law", 
    "odisha court result", "high court of orissa notification", "high court of orissa admit card"
    ],
    "pstd": [
    "pstd", "punjab state transport department", "punjab transport", "pstd recruitment", 
    "pstd exam", "punjab transport jobs", "punjab public transport", "punjab buses", 
    "pstd result", "pstd notification", "pstd admit card", "pstd career"
    ],
    "phhc": [
    "phhc", "punjab and haryana high court", "punjab haryana high court", "punjab and haryana judiciary", 
    "phhc recruitment", "punjab haryana court jobs", "phhc exam", "punjab haryana law", 
    "phhc result", "punjab haryana high court notification", "punjab haryana high court admit card"
    ],
    "mphb": [
    "mphb", "madhya pradesh housing board", "madhya pradesh housing", "madhya pradesh real estate", 
    "mp housing board recruitment", "mp housing board exam", "madhya pradesh housing jobs", "mphb result", 
    "mphb notification", "mphb admit card", "madhya pradesh housing career"
    ],
    "mppcb": [
    "mppcb", "madhya pradesh pollution control board", "madhya pradesh environment", "mppcb recruitment", 
    "mppcb exam", "mp pollution control jobs", "madhya pradesh environmental issues", "mppcb result", 
    "mppcb notification", "mppcb admit card", "mppcb career"
    ],
    "opsc": [
    "opsc", "odisha public service commission", "odisha psc", "opsc recruitment", 
    "opsc exam", "odisha public service jobs", "opsc result", "opsc notification", 
    "opsc admit card", "opsc career"
    ],
    "osssc": [
    "osssc", "odisha subordinate staff selection commission", "odisha sssc", "osssc recruitment", 
    "osssc exam", "odisha subordinate staff jobs", "osssc result", "osssc notification", 
    "osssc admit card", "osssc career"
    ],
    
    "tnusrb": [
    "tnusrb", "tamil nadu uniformed services recruitment board", "tamil nadu uniformed services", "tnusrb recruitment", 
    "tnusrb exam", "tamil nadu police recruitment", "tnusrb result", "tnusrb notification", 
    "tnusrb admit card", "tnusrb career"
    ],
    "upbeb": [
    "upbeb", "uttar pradesh basic education board", "uttar pradesh education board", "upbeb recruitment", 
    "upbeb exam", "uttar pradesh education jobs", "upbeb result", "upbeb notification", 
    "upbeb admit card", "upbeb career"
    ],
    "pscb": [
    "pscb", "punjab state cooperative bank", "punjab cooperative bank", "pscb recruitment", 
    "pscb exam", "punjab state bank jobs", "pscb result", "pscb notification", 
    "pscb admit card", "pscb career"
    ],
    "ppsc": [
    "ppsc", "punjab public service commission", "punjab psc", "ppsc recruitment", 
    "ppsc exam", "punjab public service jobs", "ppsc result", "ppsc notification", 
    "ppsc admit card", "ppsc career"
    ],
    "pprb": [
    "pprb", "punjab police recruitment board", "punjab police recruitment", "pprb recruitment", 
    "pprb exam", "punjab police jobs", "pprb result", "pprb notification", 
    "pprb admit card", "pprb career"
    ],
    "upprpb": [
    "upprpb", "uttar pradesh police recruitment and promotion board", "uttar pradesh police recruitment", 
    "upprpb recruitment", "upprpb exam", "uttar pradesh police jobs", "upprpb result", 
    "upprpb notification", "upprpb admit card", "upprpb career"
    ],
    "psssb": [
    "psssb", "punjab subordinate service selection board", "punjab sssb", "psssb recruitment", 
    "psssb exam", "punjab sssb jobs", "punjab subordinate services", "psssb result", 
    "psssb notification", "psssb admit card", "psssb career"
    ],
    
    "uppsc": [
    "uppsc", "uttar pradesh public service commission", "uttar pradesh psc", "uppsc recruitment", 
    "uppsc exam", "uttar pradesh public service jobs", "uppsc result", "uppsc notification", 
    "uppsc admit card", "uppsc career"
    ],
    "pseb": [
    "pseb", "punjab school education board", "punjab education board", "punjab school board", 
    "pseb recruitment", "pseb exam", "punjab school education jobs", "pseb result", 
    "pseb notification", "pseb admit card", "pseb career"
    ],
    "upsssc": [
    "upsssc", "uttar pradesh subordinate services selection commission", "uttar pradesh sssc", "upsssc recruitment", 
    "upsssc exam", "uttar pradesh subordinate services jobs", "upsssc result", "upsssc notification", 
    "upsssc admit card", "upsssc career"
    ],
    "tnpsc": [
    "tnpsc", "tamil nadu public service commission", "tamil nadu psc", "tnpsc recruitment", 
    "tnpsc exam", "tamil nadu public service jobs", "tnpsc result", "tnpsc notification", 
    "tnpsc admit card", "tnpsc career"
    ],
    "upsad": [
    "upsad", "uttar pradesh state agricultural department", "uttar pradesh agriculture department", "upsad recruitment", 
    "upsad exam", "uttar pradesh agriculture jobs", "upsad result", "upsad notification", 
    "upsad admit card", "upsad career"
    ],
    "rto": [
    "rto", "rajasthan transport department", "rajasthan transport", "rto recruitment", 
    "rto exam", "rajasthan transport jobs", "rto result", "rto notification", 
    "rto admit card", "rto career"
    ],
    "uppcl": [
    "uppcl", "uttar pradesh power corporation limited", "uttar pradesh power distribution", "uppcl recruitment", 
    "uppcl exam", "uttar pradesh power jobs", "uppcl result", "uppcl notification", 
    "uppcl admit card", "uppcl career"
    ],
    "dmhfw": [
    "dmhfw", "department of medical, health and family welfare", "uttar pradesh health department", "dmhfw recruitment", 
    "dmhfw exam", "uttar pradesh health jobs", "dmhfw result", "dmhfw notification", 
    "dmhfw admit card", "dmhfw career"
    ],
    "rajasthan_environment": [
    "rajasthan_environment", "rajasthan environment and climate change department", "rajasthan environment", 
    "rajasthan climate change", "rajasthan environment department", "rajasthan environment recruitment", 
    "rajasthan environment exam", "rajasthan environment jobs", "rajasthan environment result", 
    "rajasthan environment notification", "rajasthan environment admit card", "rajasthan environment career"
    ],
    "rpsc": [
    "rpsc", "rajasthan public service commission", "rajasthan psc", "rpsc recruitment", 
    "rpsc exam", "rajasthan public service jobs", "rpsc result", "rpsc notification", 
    "rpsc admit card", "rpsc career"
    ],
    "bor": [
    "bor", "board of revenue uttar pradesh", "uttar pradesh revenue board", "bor recruitment", 
    "bor exam", "uttar pradesh land revenue jobs", "bor result", "bor notification", 
    "bor admit card", "bor career"
    ],
    "crb": [
    "crb", "central recruitment board", "crb recruitment", "crb exam", 
    "central recruitment jobs", "crb result", "crb notification", 
    "crb admit card", "crb career"
    ],
    
    "rajasthan_forest": [
    "rajasthan_forest", "rajasthan forest department", "rajasthan conservation department", 
    "rajasthan forestry", "rajasthan forest recruitment", "rajasthan forest exam", 
    "rajasthan forest jobs", "rajasthan forest result", "rajasthan forest notification", 
    "rajasthan forest admit card", "rajasthan forest career"
    ],
    "rssb": [
    "rssb", "rajasthan staff selection board", "rajasthan staff board", "rssb recruitment", 
    "rssb exam", "rajasthan staff selection jobs", "rssb result", "rssb notification", 
    "rssb admit card", "rssb career"
    ],
    "upmsrb": [
    "upmsrb", "uttar pradesh medical and health services recruitment board", 
    "uttar pradesh medical recruitment", "upmsrb recruitment", "upmsrb exam", 
    "uttar pradesh health services jobs", "upmsrb result", "upmsrb notification", 
    "upmsrb admit card", "upmsrb career"
    ],
    "rajasthan_police_force": [
    "rajasthan_police_force", "rajasthan police", "rajasthan police force", 
    "rajasthan police recruitment", "rajasthan police exam", "rajasthan police jobs", 
    "rajasthan police result", "rajasthan police notification", "rajasthan police admit card", 
    "rajasthan police career"
    ],
    "upsrtc": [
    "upsrtc", "uttar pradesh state road transport corporation", "uttar pradesh transport", 
    "upsrtc recruitment", "upsrtc exam", "uttar pradesh road transport jobs", 
    "upsrtc result", "upsrtc notification", "upsrtc admit card", "upsrtc career"
    ],
    "uksssc": [
    "uksssc", "uttarakhand subordinate service selection commission", "uttarakhand sssc", 
    "uksssc recruitment", "uksssc exam", "uttarakhand subordinate services jobs", 
    "uksssc result", "uksssc notification", "uksssc admit card", "uksssc career"
    ],
    "ujvnl": [
    "ujvnl", "uttarakhand jal vidyut nigam limited", "uttarakhand electricity board", 
    "ujvnl recruitment", "ujvnl exam", "uttarakhand electricity jobs", 
    "ujvnl result", "ujvnl notification", "ujvnl admit card", "ujvnl career"
    ],
    "hcraj": [
    "hcraj", "high court of rajasthan", "rajasthan high court", "hcraj recruitment", 
    "hcraj exam", "rajasthan high court jobs", "hcraj result", "hcraj notification", 
    "hcraj admit card", "hcraj career"
    ],
    "reet": [
    "reet", "rajasthan eligibility examination for teachers", "rajasthan teacher exam", 
    "reet recruitment", "reet exam", "rajasthan teaching jobs", "reet result", 
    "reet notification", "reet admit card", "reet career"
    ],
    "rseb": [
    "rseb", "rajasthan state electricity board", "rajasthan electricity board", 
    "rseb recruitment", "rseb exam", "rajasthan electricity jobs", "rseb result", 
    "rseb notification", "rseb admit card", "rseb career"
    ],
    "rsrtc": [
    "rsrtc", "rajasthan state road transport corporation", "rajasthan road transport", 
    "rsrtc recruitment", "rsrtc exam", "rajasthan state transport jobs", 
    "rsrtc result", "rsrtc notification", "rsrtc admit card", "rsrtc career"
    ],
    "uphesc": [
    "uphesc", "uttar pradesh higher education service commission", "up higher education", 
    "uphesc recruitment", "uphesc exam", "uttar pradesh higher education jobs", 
    "uphesc result", "uphesc notification", "uphesc admit card", "uphesc career"
    ],
    
    "uppcb": [
    "uppcb", "uttar pradesh pollution control board", "uttar pradesh pollution", 
    "uppcb recruitment", "uppcb exam", "uttar pradesh pollution control jobs", 
    "uppcb result", "uppcb notification", "uppcb admit card", "uppcb career"
    ],
    "agri": [
    "agri", "rajasthan agriculture department", "rajasthan agriculture", "rajasthan farming", 
    "rajasthan agriculture recruitment", "rajasthan agricultural jobs", "rajasthan farming jobs", 
    "rajasthan agriculture exam", "rajasthan agriculture result", "rajasthan agriculture notification", 
    "rajasthan agriculture admit card", "rajasthan agriculture career"
    ],
    
    "mhset": [
    "mhset", "maharashtra state eligibility test", "maharashtra eligibility test", 
    "maharashtra assistant professor exam", "mhset recruitment", "mhset exam", 
    "maharashtra professor jobs", "mhset result", "mhset notification", "mhset admit card", 
    "mhset career"
    ],
    "hpcpmt": [
    "hpcpmt", "himachal pradesh combined pre-medical test", "himachal pradesh medical exam", 
    "hpcpmt recruitment", "hpcpmt exam", "himachal pradesh medical jobs", 
    "hpcpmt result", "hpcpmt notification", "hpcpmt admit card", "hpcpmt career"
    ],
    
    "nta": [
    "nta", "national testing agency", "nta recruitment", "nta exam", 
    "national testing agency exam", "nta result", "nta notification", 
    "nta admit card", "nta career"
    ],
    "ojas": [
    "ojas", "online job application system", "ojas recruitment", 
    "ojas exam", "ojas result", "ojas notification", 
    "ojas admit card", "ojas career"
    ],
    "upjee": [
    "upjee", "uttar pradesh joint entrance examination", "upjee exam", 
    "uttar pradesh jee", "upjee recruitment", "upjee diploma admission", 
    "upjee result", "upjee notification", "upjee admit card", "upjee career"
    ],
    "gsssb": [
    "gsssb", "gujarat subordinate service selection board", "gsssb recruitment", 
    "gsssb exam", "gujarat sssb jobs", "gsssb result", 
    "gsssb notification", "gsssb admit card", "gsssb career"
    ],
    "trb": [
    "trb", "teachers recruitment board", "trb recruitment", "trb exam", 
    "trb teacher recruitment", "trb result", "trb notification", 
    "trb admit card", "trb career"
    ],
    "utet": [
    "utet", "uttarakhand teacher eligibility test", "utet exam", 
    "uttarakhand tet", "utet recruitment", "utet result", 
    "utet notification", "utet admit card", "utet career"
    ],
    "mahatet": [
    "mahatet", "maharashtra teacher eligibility test", "mahatet exam", 
    "maharashtra tet", "mahatet recruitment", "mahatet result", 
    "mahatet notification", "mahatet admit card", "mahatet career"
    ],
    "gtet": [
    "gtet", "gujarat teacher eligibility test", "gtet exam", 
    "gujarat tet", "gtet recruitment", "gtet result", 
    "gtet notification", "gtet admit card", "gtet career"
    ],
    
    "ojee": [
    "ojee", "odisha joint entrance examination", "ojee exam", 
    "odisha entrance exam", "ojee recruitment", "ojee result", 
    "ojee notification", "ojee admit card", "ojee career"
    ],
    "aptet": [
    "aptet", "andhra pradesh teacher eligibility test", "aptet exam", 
    "andhra pradesh tet", "aptet recruitment", "aptet result", 
    "aptet notification", "aptet admit card", "aptet career"
    ],
    "rsldc": [
    "rsldc", "rajasthan state livelihoods development corporation", 
    "rsldc recruitment", "rsldc jobs", "rsldc result", 
    "rsldc notification", "rsldc admit card", "rsldc career"
    ],
    "otet": [
    "otet", "odisha teacher eligibility test", "otet exam", 
    "odisha tet", "otet recruitment", "otet result", 
    "otet notification", "otet admit card", "otet career"
    ],
    "apeamcet": [
    "apeamcet", "andhra pradesh engineering agriculture medical common entrance test", 
    "apeamcet exam", "andhra pradesh eamcet", "apeamcet recruitment", 
    "apeamcet result", "apeamcet notification", "apeamcet admit card", "apeamcet career"
    ],
    
    "mhtcet": [
    "mhtcet", "maharashtra common entrance test", "mhtcet exam", 
    "maharashtra cet", "mhtcet recruitment", "mhtcet result", 
    "mhtcet notification", "mhtcet admit card", "mhtcet career"
    ],
    "hstes": [
    "hstes", "haryana state technical education society", 
    "hstes recruitment", "hstes jobs", "hstes result", 
    "hstes notification", "hstes admit card", "hstes career"
    ],
    "pstet": [
    "pstet", "punjab state teacher eligibility test", "pstet exam", 
    "punjab tet", "pstet recruitment", "pstet result",
    "pstet notification", "pstet admit card", "pstet career"
    ],
    "maharashtrapolice": [
    "maharashtrapolice", "maharashtra police", "maharashtra police recruitment", 
    "maharashtra police jobs", "maharashtra police exam", "maharashtra police result", 
    "maharashtra police notification", "maharashtra police admit card", "maharashtra police career"
    ],
    "pspcl": [
    "pspcl", "punjab state power corporation limited", "pspcl recruitment", 
    "pspcl jobs", "pspcl result", "pspcl notification", 
    "pspcl admit card", "pspcl career"
    ],
    "rsmssb": [
    "rsmssb", "rajasthan subordinate and ministerial services selection board", 
    "rsmssb recruitment", "rsmssb jobs", "rsmssb result", 
    "rsmssb notification", "rsmssb admit card", "rsmssb career"
    ]
}
    
    return variations