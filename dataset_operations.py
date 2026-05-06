def get_title_code(title):
    if type(title) == float:
        return 'NO_TITLE', 0
    title = title.lower()
    if 'open to work' in title or 'open to opportunities' in title or 'open to new opportunities' in title \
      or 'open to entry level' in title or 'looking for a new opportunity' in title or 'employment opportunity' in title \
      or 'experience with every given opportunity' in title or 'looking for new opportunities' in title \
      or 'looking for new carrier' in title or 'looking for opportunities' in title or 'looking for a new path' in title \
      or 'looking for a long term career' in title or 'looking for new recruiting opportunities' in title \
      or 'looking for professional opportunities' in title or 'looking for a full time position' in title \
      or 'looking for writing opportunities' in title or 'job searching' in title or 'seeking new opportunities' in title \
      or 'seeking opportunities' in title:
        return 'OPEN', 0
    ### WHITE COLLAR ###
    elif 'account manager' in title:   
        return 'WC00', 0
    elif 'ai engineering' in title or 'ai engineer' in title or 'ai frameworks engineer' in title \
      or 'ai research engineer' in title or 'ai model designer' in title or 'ai product designer' in title or 'ai designer' in title:
        return 'WC01', 1
    elif 'application developer' in title or 'app developer' in title or 'development engineer' in title \
      or 'application engineer' in title or 'applications engineer' in title:
        return 'WC02', 2
    elif 'applied scientist' in title:   
        return 'WC03', 3
    elif 'asic design engineer' in title:   
        return 'WC04', 4
    elif 'backend developer' in title or 'back end developer' in title or 'back-end developer' in title \
      or 'backend engineer' in title or 'back end engineer' in title or 'back-end engineer' in title:   
        return 'WC05', 5
    elif 'business analyst' in title or 'business intelligence analyst' in title or 'business technology analyst' in title \
      or 'business systems analyst' in title or 'business strategy analyst' in title or 'bi analyst' in title \
      or 'business analytics' in title or ('business' in title and 'analyst' in title):
        return 'WC06', 6
    elif 'business intelligence engineer' in title or 'bi engineer' in title or 'bi developer' in title \
      or 'business intelligence developer' in title or 'bi and analytics engineer' in title or 'business intelligence' in title:
        return 'WC07', 7
    elif 'chemical engineer' in title:   
        return 'WC08', 8
    elif 'civil engineer' in title or 'civil design engineer' in title or 'cilvil engineer' in title \
      or 'civil/structural/transportation engineer' in title:
        return 'WC09', 9
    elif 'cloud engineer' in title or 'cloud infrastructure engineer' in title or 'cloud and innovation engineer' in title \
      or 'cloud architect' in title:
        return 'WC10', 10
    elif 'computer engineer' in title:   
        return 'WC11', 11
    elif 'consultant' in title:   
        return 'WC12', 12
    elif 'content designer' in title or 'content developer' in title or 'content producer' in title:   
        return 'WC13', 13
    elif 'content marketing' in title or 'content marketer' in title:   
        return 'WC14', 14
    elif 'content strategist' in title:   
        return 'WC15', 15
    elif 'customer engineer' in title:   
        return 'WC16', 16
    elif 'data analyst' in title or 'data insights analyst' in title or 'data and systems analyst' in title \
      or 'data intelligence analyst' in title or 'data quality analyst' in title or 'data solutions analyst' in title \
      or 'data analytics' in title or ('data' in title and 'analyst' in title) or ('data' in title and 'analytics' in title):   
        return 'WC17', 17
    elif 'data architect' in title:   
        return 'WC18', 18
    elif 'data engineer' in title:   
        return 'WC19', 19
    elif 'data scientist' in title or 'data science' in title:   
        return 'WC20', 20
    elif 'database administrator' in title or 'database administration' in title or 'dba' in title:   
        return 'WC21', 21
    elif 'database engineer' in title:  
        return 'WC22', 22
    elif 'design engineer' in title or 'design verification engineer' in title or 'design/debug engineer' in title:   
        return 'WC23', 23
    elif 'devops engineer' in title or 'devsecops engineer' in title or 'devops' in title:   
        return 'WC24', 24
    elif 'distinguished engineer' in title:   
        return 'WC25', 25
    elif 'dotnet developer' in title or '.net developer' in title:   
        return 'WC26', 26
    elif 'ecommerce' in title or 'e-commerce' in title:   
        return 'WC27', 27
    elif 'electrical engineer' in title or 'electronic engineer' in title or 'electronics engineer' in title:   
        return 'WC28', 28
    elif 'energy analyst' in title or 'energy & chemicals' in title:   
        return 'WC29', 29
    elif 'environmental engineer' in title or 'environmental scientist' in title or 'environmental compliance engineer' in title:
        return 'WC30', 30
    elif 'financial analyst' in title or 'finance project analyst' in title or 'financial analytics' in title \
      or 'finance analyst' in title or 'finance professional' in title:
        return 'WC31', 31
    elif 'firmware developer' in title or 'firmware engineer' in title:   
        return 'WC32', 32
    elif 'frontend developer' in title or 'front-end developer' in title or 'front end developer' in title \
      or 'frontend engineer' in title or 'front-end engineer' in title or 'front end engineer' in title \
      or 'javascript developer' in title or 'react developer' in title:   
        return 'WC33', 33
    elif 'fullstack developer' in title or 'full stack developer' in title or 'full-stack developer' in title \
      or 'fullstack engineer' in title or 'full stack engineer' in title or 'full-stack engineer' in title:   
        return 'WC34', 34
    elif 'graphic designer' in title:   
        return 'WC35', 35
    elif 'hardware engineer' in title or 'hardware design engineer' in title:   
        return 'WC36', 36
    elif 'investment banking analyst' in title:   
        return 'WC37', 37
    elif 'it engineer' in title or 'it support engineer' in title or 'information technology engineer' in title \
      or 'it architect' in title:
        return 'WC38', 38
    elif 'java developer' in title or 'java/guidewire developer' in title \
      or 'java full stack aws developer' in title or 'java microservices developer' in title or 'java/j2ee developer' in title:   
        return 'WC39', 39
    elif 'machine learning engineer' in title or 'machine learning scientist' in title or 'ml engineer' in title \
      or 'machine learning' in title or 'deep learning engineer' in title or title.startswith('ml'):
        return 'WC40', 40
    elif 'marketing analyst' in title or 'market research analyst' in title or 'market analyst' in title \
      or 'marketing specialist' in title or 'marketing strategist' in title or 'marketing analytics' in title \
      or 'marketing execution analyst' in title or 'marketing executive' in title or 'market expert' in title \
      or 'marketing professional' in title or 'growth marketing' in title or 'brand marketing' in title \
      or 'global marketing' in title or 'salesforce marketing' in title or 'lifecycle marketing' in title:
        return 'WC41', 41
    elif 'mechanical engineer' in title or 'mechanical display engineer' in title or 'mechanical metrology engineer' in title:
        return 'WC42', 42
    elif 'mobile developer' in title or 'ios developer' in title or 'android developer' in title:   
        return 'WC43', 43
    elif 'network administrator' in title or 'network administration' in title:   
        return 'WC44', 44
    elif 'network engineer' in title or 'networks engineer' in title or 'network development engineer' in title \
      or 'network.engineer' in title or 'infrastructure engineer' in title or 'infrastructure services engineer' in title \
      or 'network consulting engineer' in title:
        return 'WC45', 45
    elif 'network specialist' in title or 'security specialist' in title:   
        return 'WC46', 46
    elif 'operations analyst' in title or 'operations engineer' in title:  
        return 'WC47', 47
    elif 'partner specialist' in title:   
        return 'WC48', 48
    elif 'petroleum engineer' in title:   
        return 'WC49', 49
    elif 'platform engineer' in title or 'platform developer' in title or 'plaform engineer' in title:   
        return 'WC50', 50
    elif 'process engineer' in title:   
        return 'WC51', 51
    elif 'product manager' in title or 'product development engineer' in title or 'product marketing manager' in title \
      or 'product analytics' in title:
        return 'WC52', 52
    elif 'product marketing' in title or 'product marketer' in title or 'digital marketing' in title \
      or 'digital marketer' in title or 'digital advertising' in title:   
        return 'WC53', 53
    elif 'program manager' in title:   
        return 'WC54', 54
    elif 'project manager' in title or 'project mananger' in title:   
        return 'WC55', 55
    elif 'python developer' in title:   
        return 'WC56', 56
    elif 'qa analyst' in title:   
        return 'WC57', 57
    elif 'qa engineer' in title or 'quality assurance' in title or 'quality engineer' in title \
      or 'qa automation engineer' in title or 'qa lead automation engineer' in title or 'qa mobile tester engineer' in title \
      or 'qa lead engineer' in title or 'qe engineering' in title or 'automation verification engineer' in title:
        return 'WC58', 58
    elif 'research engineer' in title:   
        return 'WC59', 59
    elif 'sales development representative' in title:   
        return 'WC60', 60
    elif 'sales engineer' in title:   
        return 'WC61', 61
    elif 'salesforce developer' in title or 'salesforce admin and developer' in title:   
        return 'WC62', 62
    elif 'scrum master' in title:   
        return 'WC63', 63
    elif 'security engineer' in title:   
        return 'WC64', 64
    elif 'seo specialist' in title or 'seo analyst' in title:   
        return 'WC65', 65
    elif 'servicenow developer' in title or 'servicenow grc/irm-secops architect' in title:   
        return 'WC66', 66
    elif 'sharepoint developer' in title:   
        return 'WC67', 67
    elif 'software engineer' in title or 'software development engineer' in title or 'software developer' in title \
      or 'software / firmware engineer' in title or 'softwear developer' in title or 'sofware developer' in title \
      or 'software dev engineer' in title or 'software devlopment engineer' in title \
      or 'software application development engineer' in title or 'software applications development engineer' in title \
      or 'software development emulator' in title or title.startswith('sde'):   
        return 'WC68', 68
    elif 'solution architect' in title or 'solutions architect' in title or 'solution developer' in title \
      or 'solution engineer' in title or 'solutions engineer' in title:
        return 'WC69', 69
    elif 'staff engineer' in title:   
        return 'WC70', 70
    elif 'supply chain solutions' in title or 'supply chain planning' in title or 'supply chain analyst' in title \
      or 'supply chain program analyst' in title:
        return 'WC71', 71
    elif 'support engineer' in title:   
        return 'WC72', 72
    elif 'system administrator' in title or 'systems administrator' in title:   
        return 'WC73', 73
    elif 'system engineer' in title or 'systems engineer' in title or 'system admin/engineer' in title \
      or 'system development engineer' in title or 'systems development engineer' in title:   
        return 'WC74', 74
    elif 'technical analyst' in title or 'technical solution analyst' in title or 'technical solutions analyst' in title:
        return 'WC75', 75
    elif 'test engineer' in title or 'test automation engineer' in title or 'test automation developer' in title \
      or 'automation engineer' in title or 'test development engineer' in title or 'test r&d engineer' in title \
      or 'test r & d engineer' in title or 'test product development engineer' in title or 'software test' in title:
        return 'WC76', 76
    elif 'user experience designer' in title or 'user experience, visual designer' in title \
      or 'user experience researcher & designer' in title or 'user experience engineer' in title \
      or 'user experience (ux) designer' in title or 'ux/ui designer' in title or 'ux ui designer' in title \
      or 'user experience researcher' in title or 'user experience & brand designer' in title \
      or 'ux visual & motion designer' in title or 'ui/ux visual designer' in title or 'ux/visual designer' in title \
      or 'ux designer' in title or 'ux engineer' in title or 'ux/ ui designer' in title or 'product designer' in title \
      or 'user interface developer' in title or 'ui developer' in title:   
        return 'WC77', 77
    elif 'web developer' in title or 'web production developer' in title:   
        return 'WC78', 78
    ### BLUE COLLAR ###
    elif 'academic advisor' in title or 'academic advising' in title:   
        return 'BC00', 0
    elif 'account executive' in title:   
        return 'BC01', 1
    elif 'account strategist' in title:   
        return 'BC02', 2
    elif 'accountant' in title:   
        return 'BC03', 3
    elif 'actuary' in title:   
        return 'BC04', 4
    elif 'admission counselor' in title or 'admissions counselor' in title:   
        return 'BC05', 5
    elif 'auditor' in title or 'audit associate' in title:   
        return 'BC06', 6
    elif 'baker' in title:   
        return 'BC07', 7
    elif 'barista' in title:   
        return 'BC08', 8
    elif 'bartender' in title:   
        return 'BC09', 9
    elif 'bookkeeper' in title:   
        return 'BC10', 10
    elif 'beauty advisor' in title:   
        return 'BC11', 11
    elif 'claims adjuster' in title:   
        return 'BC12', 12
    elif 'compliance officer' in title or 'compliance risk officer' in title or 'compliance/operations officer' in title \
      or 'compliance risk management officer' in title:
        return 'BC13', 13
    elif 'corporate counsel' in title:   
        return 'BC14', 14
    elif 'curriculum developer' in title:   
        return 'BC15', 15
    elif 'customer service manager' in title:   
        return 'BC16', 16
    elif 'delivery driver' in title:   
        return 'BC17', 17
    elif 'dental assistant' in title or 'dental assisting' in title:   
        return 'BC18', 18
    elif 'electrician' in title:   
        return 'BC19', 19
    elif 'executive assistant' in title or 'executive & administrative assistant' in title:   
        return 'BC20', 20
    elif 'food scientist' in title:   
        return 'BC21', 21
    elif 'help desk support' in title or 'help desk analyst' in title:   
        return 'BC22', 22
    elif 'inside sales' in title:   
        return 'BC23', 23
    elif 'insurance agent' in title:   
        return 'BC24', 24
    elif 'interaction designer' in title:   
        return 'BC25', 25
    elif 'librarian' in title:   
        return 'BC26', 26
    elif 'medical assistant' in title:   
        return 'BC27', 27
    elif 'merchandiser' in title:   
        return 'BC28', 28
    elif 'nurse' in title:   
        return 'BC29', 29
    elif 'office administrator' in title:   
        return 'BC30', 30
    elif 'outside sales' in title:   
        return 'BC31', 31
    elif 'paralegal' in title:   
        return 'BC32', 32
    elif 'paramedic' in title:   
        return 'BC33', 33
    elif 'police officer' in title or 'police official' in title:   
        return 'BC34', 34
    elif 'policy analyst' in title:   
        return 'BC35', 35
    elif 'principal' in title:   
        return 'BC36', 36
    elif 'program coordinator' in title:   
        return 'BC37', 37
    elif 'psychologist' in title:   
        return 'BC38', 38
    elif 'real estate agent' in title:   
        return 'BC39', 39
    elif 'recruit' in title:   
        return 'BC40', 40
    elif 'sales associate' in title or 'sales representative' in title:   
        return 'BC41', 41
    elif 'school counselor' in title:  
        return 'BC42', 42
    elif 'secretary' in title:   
        return 'BC43', 43
    elif 'security officer' in title or 'security guard' in title:   
        return 'BC44', 44
    elif 'social worker' in title or 'lmsw' in title:   
        return 'BC45', 45
    elif 'supervisor' in title:   
        return 'BC46', 46
    elif 'talent assistant' in title:   
        return 'BC47', 47
    elif 'teacher' in title:   
        return 'BC48', 48
    elif 'technician' in title:   
        return 'BC49', 49
    elif 'therapist' in title:   
        return 'BC50', 50
    elif 'touring assistant' in title:   
        return 'BC51', 51
    elif 'transportation planner' in title:   
        return 'BC52', 52
    elif 'underwriter' in title:   
        return 'BC53', 53
    elif 'urban planner' in title:   
        return 'BC54', 54
    elif 'vice president' in title:   
        return 'BC55', 55
    elif 'welder' in title:   
        return 'BC56', 56
    ### UNCATEGORIZED TITLE ###
    else:   
        return 'UNCT', 0
        
def get_title_snr_code(title):
    if type(title) == float:
        return 'NO_TITLE'
    title = title.lower()
    if 'principal' in title:
        return 'PRINCIPAL'
    elif 'senior staff' in title or 'sr. staff' in title:
        return 'SENIOR_STAFF'
    elif 'staff' in title:
        return 'STAFF'
    elif 'senior' in title or 'sr.' in title:
        return 'SENIOR'
    elif 'associate' in title:
        return 'ASSOCIATE'
    elif 'junior' in title:
        return 'JUNIOR'
    else:
        return 'NO_SENIORITY'
    
def get_position_code(pos):
    pos = pos.lower().replace('&','and')
    ### WHITE COLLAR POSITIONS ###
    if 'account manager' in pos:   
        return 'WC00', 0
    elif 'ai engineer' in pos or 'ai frameworks engineer' in pos:   
        return 'WC01', 1
    elif 'application engineer' in pos or 'applications engineer' in pos or 'application developer' in pos:   
        return 'WC02', 2
    elif 'automation test' in pos:   
        return 'WC03', 3
    elif 'backend developer' in pos or 'back end developer' in pos:   
        return 'WC04', 4
    elif 'business analyst' in pos or 'business intelligence analyst' in pos or 'business systems analyst' in pos \
      or 'business system analyst' in pos or 'business operations analyst' in pos or 'business tech analyst' in pos \
      or 'business technology analyst' in pos or 'business practice analyst' in pos or 'analyst.business' in pos \
      or 'business strategy analyst' in pos or 'business  analyst' in pos or 'business process analyst' in pos \
      or 'business management program analyst' in pos or 'business integrity analyst' in pos or 'analyst, business' in pos:
        return 'WC05', 5
    elif 'business intelligence engineer' in pos or 'bi engineer' in pos or 'business intelligence developer' in pos \
      or 'business intelligence lead engineer' in pos or 'business intelligence and analytics engineer' in pos \
      or 'bie' in pos:
        return 'WC06', 6
    elif 'chemical engineer' in pos:   
        return 'WC07', 7
    elif 'civil engineer' in pos:   
        return 'WC08', 8
    elif 'cloud engineer' in pos or 'cloud deployment engineer' in pos or 'cloud and innovation engineer' in pos:
        return 'WC09', 9
    elif 'consultant' in pos:   
        return 'WC10', 10
    elif 'content designer' in pos:   
        return 'WC11', 11
    elif 'content producer' in pos:   
        return 'WC12', 12
    elif 'content strategist' in pos:   
        return 'WC13', 13
    elif 'customer engineer' in pos:   
        return 'WC14', 14
    elif 'data analyst' in pos or 'data analytics and reporting analyst' in pos or 'data systems analyst' in pos \
      or 'data science analyst' in pos or 'data intelligence analyst' in pos or 'data quality analyst' in pos \
      or 'data operations analyst' in pos or 'data governance analyst' in pos or 'data protection analyst' in pos \
      or 'data center analyst' in pos or 'data security analyst' in pos or 'data integrity analyst' in pos \
      or 'data and reporting analyst' in pos or 'data and compliance analyst' in pos or 'data insights analyst' in pos \
      or 'data reference analyst' in pos or 'analyst, data' in pos or 'analyst - data' in pos \
      or 'data quality and sales operations analyst' in pos or ('analyst' in pos and 'data' in pos):
        return 'WC15', 15
    elif 'data architect' in pos:   
        return 'WC16', 16
    elif 'data engineer' in pos:   
        return 'WC17', 17
    elif 'data scientist' in pos or 'data and applied scientist' in pos or 'applied scientist' in pos \
      or 'data and systems analyst' in pos or 'data science engineer' in pos or 'data science and engineering' in pos:
        return 'WC18', 18
    elif 'database administrator' in pos or 'database administration' in pos:   
        return 'WC19', 19
    elif 'database engineer' in pos:   
        return 'WC20', 20
    elif 'design engineer' in pos or 'design verification engineer' in pos:   
        return 'WC21', 21
    elif 'devops engineer' in pos or 'devsecops' in pos or 'devops' in pos:   
        return 'WC22', 22
    elif 'distinguished engineer' in pos:   
        return 'WC23', 23
    elif 'ecommerce' in pos or 'e-commerce' in pos:   
        return 'WC24', 24
    elif 'electrical engineer' in pos:   
        return 'WC25', 25
    elif 'energy analyst' in pos or 'energy markets analyst' in pos:   
        return 'WC26', 26
    elif 'environmental engineer' in pos or 'environmental compliance engineer' in pos \
      or 'environmental consulting engineer' in pos:
        return 'WC27', 27
    elif 'financial analyst' in pos or 'finance operations analyst' in pos or 'finance project analyst' in pos \
      or 'finance analyst' in pos:   
        return 'WC28', 28
    elif 'frontend developer' in pos or 'front-end developer' in pos or 'front end developer' in pos \
      or 'frontend engineer' in pos or 'front-end engineer' in pos or 'front end engineer' in pos or 'react developer' in pos:
        return 'WC29', 29
    elif 'fullstack developer' in pos or 'full stack developer' in pos or 'full-stack developer' in pos \
      or 'fullstack engineer' in pos or 'full stack engineer' in pos or 'full-stack javascript developer' in pos \
      or 'full-stack react native developer' in pos:   
        return 'WC30', 30
    elif 'graphic designer' in pos:   
        return 'WC31', 31
    elif 'hardware engineer' in pos or 'hardware dev engineer' in pos or 'hardware development engineer' in pos:
        return 'WC32', 32
    elif 'help desk' in pos or 'helpdesk' in pos:   
        return 'WC33', 33
    elif 'infrastructure engineer' in pos:   
        return 'WC34', 34
    elif 'investment banking analyst' in pos:   
        return 'WC35', 35
    elif 'it architect' in pos or 'information technology architect' in pos:   
        return 'WC36', 36
    elif 'it support engineer' in pos or 'it engineer' in pos or 'information technology engineer' in pos \
      or 'information technology operations engineer' in pos or 'information architect' in pos:   
        return 'WC37', 37
    elif 'java developer' in pos or 'java/j2ee developer' in pos:   
        return 'WC38', 38
    elif 'machine learning engineer' in pos or 'machine learning scientist' in pos \
      or 'machine learning research engineer' in pos or 'machine learning and relevance engineer' in pos \
      or 'machine learning platform engineer' in pos or 'machine learning developer' in pos or 'deep learning/machine learning' in pos \
      or 'ml engineer' in pos or 'machine learning' in pos:   
        return 'WC39', 39
    elif 'marketing analyst' in pos or 'market analyst' in pos or 'market research and analysis' in pos \
      or 'market research manager' in pos or 'marketing operations analyst' in pos or 'market research analyst' in pos \
      or 'marketing execution analyst' in pos or 'marketing research analyst' in pos or 'marketing campaign analyst' in pos \
      or 'analyst, marketing' in pos:   
        return 'WC40', 40
    elif 'mechanical engineer' in pos:   
        return 'WC41', 41
    elif 'mobile developer' in pos or 'ios developer' in pos or 'ios engineer' in pos or 'ios/tvos engineer' in pos \
      or 'android developer' in pos or 'android engineer' in pos:
        return 'WC42', 42
    elif 'network administrator' in pos or 'network systems administrator' in pos:   
        return 'WC43', 43
    elif 'network engineer' in pos or 'network support engineer' in pos or 'network development engineer' in pos \
      or 'network consulting engineer' in pos:
        return 'WC44', 44
    elif 'petroleum engineer' in pos:   
        return 'WC45', 45
    elif 'platform engineer' in pos:   
        return 'WC46', 46
    elif 'policy analyst' in pos:   
        return 'WC47', 47
    elif 'process engineer' in pos:   
        return 'WC48', 48
    elif 'product designer' in pos or 'production engineer' in pos or 'product development engineer' in pos:
        return 'WC49', 49
    elif 'product manager' in pos or 'product engineering manager' in pos:   
        return 'WC50', 50
    elif 'program manager' in pos or 'program mgmt manager' in pos:   
        return 'WC51', 51
    elif 'project manager' in pos or 'project mananger' in pos:   
        return 'WC52', 52
    elif 'python developer' in pos:   
        return 'WC53', 53
    elif 'quality assurance analyst' in pos or 'qa analyst' in pos:   
        return 'WC54', 54
    elif 'quality assurance engineer' in pos or 'quality assurance specialist' in pos or 'quality engineer' in pos \
      or 'qa automation engineer' in pos or 'quality assurance automation engineer' in pos or 'qa tester engineer' in pos:
        return 'WC55', 55
    elif 'research engineer' in pos or 'research scientist' in pos:   
        return 'WC56', 56
    elif 'sales development representative' in pos:   
        return 'WC57', 57
    elif 'sales engineer' in pos:   
        return 'WC58', 58
    elif 'salesforce developer' in pos or 'salesforce admin and developer' in pos:   
        return 'WC59', 59
    elif 'security engineer' in pos:   
        return 'WC60', 60
    elif 'seo analyst' in pos or 'search engine optimization analyst' in pos or 'search engine optimization specialist' in pos:
        return 'WC61', 61
    elif 'service management' in pos:   
        return 'WC62', 62
    elif 'sharepoint developer' in pos:   
        return 'WC63', 63
    elif 'site reliability engineer' in pos:   
        return 'WC64', 64
    elif 'software qa engineer' in pos or 'qa engineer' in pos:   
        return 'WC65', 65
    elif 'software developer' in pos or 'software engineer' in pos or 'software development engineer' in pos \
      or 'software dev engineer' in pos or 'software analyst and developer' in pos or 'softwear developer' in pos \
      or 'engineer software' in pos or 'software firmware engineer' in pos or 'software  engineer' in pos \
      or 'software graphics engineer' in pos or 'firmware engineer' in pos or 'firmware development engineer' in pos \
      or 'software application development engineer' in pos or 'software build engineer' in pos \
      or 'software devlopment engineer' in pos:   
        return 'WC66', 66
    elif 'software test engineer' in pos or 'test engineer' in pos or 'test automation engineer' in pos \
      or 'test product development engineer' in pos or 'test technology engineer' in pos or 'test r and d engineer' in pos \
      or 'software test' in pos:
        return 'WC67', 67
    elif 'solutions engineer' in pos or 'solution engineer' in pos or 'solutions architect' in pos or 'solution architect' in pos:
        return 'WC68', 68
    elif 'staff engineer' in pos:   
        return 'WC69', 69
    elif 'supply chain analyst' in pos or 'supply chain solutions analyst' in pos or 'supply chain planning analyst' in pos \
      or 'supply chain associate analyst' in pos or 'supply chain program analyst' in pos or 'supply chain procurement analyst' in pos \
      or 'supply chain planning, mrp analyst' in pos:
        return 'WC70', 70
    elif 'support engineer' in pos or 'technical support engineer' in pos:   
        return 'WC71', 71
    elif 'system administrator' in pos:   
        return 'WC72', 72
    elif 'system engineer' in pos or 'systems engineer' in pos or 'systems admin/engineer' in pos \
      or 'system development engineer' in pos or 'system admin/engineer' in pos or 'systems development engineer' in pos:
        return 'WC73', 73
    elif 'technical engineer' in pos or 'technical analyst' in pos or 'technical solution analyst' in pos \
      or 'technical solutions analyst' in pos:
        return 'WC74', 74
    elif 'user experience designer' in pos or 'ux designer' in pos or 'interaction designer (ux)' in pos \
      or 'ux/ui designer' in pos or 'ux engineer' in pos or 'ui developer' in pos or 'user experience engineer' in pos \
      or 'ux researcher' in pos:
        return 'WC75', 75
    elif 'web developer' in pos or 'web production developer' in pos or 'website developer' in pos \
      or 'web solutions engineer' in pos or 'web apps' in pos:
        return 'WC76', 76
    ### BLUE COLLAR POSITIONS ###
    elif 'account executive' in pos:   
        return 'BC00', 0
    elif 'accountant' in pos:   
        return 'BC01', 1
    elif 'actuary' in pos:   
        return 'BC02', 2
    elif 'admission counselor' in pos or 'admissions counselor' in pos:   
        return 'BC03', 3
    elif 'auditor' in pos:   
        return 'BC04', 4
    elif 'barista' in pos:   
        return 'BC05', 5
    elif 'bartender' in pos:   
        return 'BC06', 6
    elif 'beauty advisor' in pos:   
        return 'BC07', 7
    elif 'boilermaker' in pos:   
        return 'BC08', 8
    elif 'bookkeeper' in pos:   
        return 'BC09', 9
    elif 'claims adjuster' in pos:   
        return 'BC10', 10
    elif 'compliance officer' in pos or 'compliance business control officer' in pos:   
        return 'BC11', 11
    elif 'corporate counsel' in pos:   
        return 'BC12', 12
    elif 'curriculum developer' in pos:   
        return 'BC13', 13
    elif 'delivery driver' in pos:   
        return 'BC14', 14
    elif 'dental assistant' in pos:   
        return 'BC15', 15
    elif 'electrician' in pos:   
        return 'BC16', 16
    elif 'food scientist' in pos:   
        return 'BC17', 17
    elif 'inside sales' in pos:   
        return 'BC18', 18
    elif 'insurance agent' in pos:   
        return 'BC19', 19
    elif 'legal secretary' in pos:   
        return 'BC20', 20
    elif 'librarian' in pos:   
        return 'BC21', 21
    elif 'medical assistant' in pos:   
        return 'BC22', 22
    elif 'merchandiser' in pos:   
        return 'BC23', 23
    elif 'nurse' in pos:   
        return 'BC24', 24
    elif 'office administrator' in pos:   
        return 'BC25', 25
    elif 'outside sales' in pos:   
        return 'BC26', 26
    elif 'paralegal' in pos:   
        return 'BC27', 27
    elif 'paramedic' in pos:   
        return 'BC28', 28
    elif 'police officer' in pos:   
        return 'BC29', 29
    elif 'principal' in pos:   
        return 'BC30', 30
    elif 'program coordinator' in pos:   
        return 'BC31', 31
    elif 'real estate agent' in pos:   
        return 'BC32', 32
    elif 'recruit' in pos:   
        return 'BC33', 33
    elif 'retail sales' in pos:   
        return 'BC34', 34
    elif 'sales associate' in pos:   
        return 'BC35', 35
    elif 'school counselor' in pos:   
        return 'BC36', 36
    elif 'school psychologist' in pos:   
        return 'BC37', 37
    elif 'security officer' in pos or 'security guard' in pos:   
        return 'BC38', 38
    elif 'social worker' in pos:   
        return 'BC39', 39
    elif 'supervisor' in pos:   
        return 'BC40', 40
    elif 'talent assistant' in pos or 'assistant, talent' in pos:   
        return 'BC41', 41
    elif 'tax advisor' in pos:   
        return 'BC42', 42
    elif 'teacher' in pos:   
        return 'BC43', 43
    elif 'technician' in pos:   
        return 'BC44', 44
    elif 'therapist' in pos:   
        return 'BC45', 45
    elif 'touring assistant' in pos or ('touring' in pos and 'assistant' in pos):   
        return 'BC46', 46
    elif 'transportation planner' in pos:   
        return 'BC47', 47
    elif 'underwriter' in pos:   
        return 'BC48', 48
    elif 'urban planner' in pos:   
        return 'BC49', 49
    elif 'vice president' in pos:   
        return 'BC50', 50
    elif 'welder' in pos:   
        return 'BC51', 51
    ### UNCATEGORIZED POSITIONS ###
    else:   
        return 'UNCT', 0
        
def get_position_snr_code(pos):
    pos = pos.lower()
    if 'principal' in pos:
        return 'PRINCIPAL'
    elif 'senior staff' in pos or 'sr. staff' in pos:
        return 'SENIOR_STAFF'
    elif 'staff' in pos:
        return 'STAFF'
    elif 'senior' in pos or 'sr.' in pos:
        return 'SENIOR'
    elif 'associate' in pos:
        return 'ASSOCIATE'
    elif 'junior' in pos:
        return 'JUNIOR'
    else:
        return 'NO_SENIORITY'
        
def get_emp_type_coef(emp):
    if type(emp) == float:
        return 'NO_EMP_TYPE', 0.10
    elif emp == 'Full-time' or emp == 'Permanent Full-time' or emp == 'Permanent':
        return 'FULL_TIME', 0.99
    elif emp == 'Part-time':
        return 'PART_TIME', 0.60
    elif emp == 'Contract':
        return 'CONTRACT', 0.50
    elif emp == 'Self-employed':
        return 'SELF_EMPLOYED', 0.45
    elif emp == 'Freelance':
        return 'FREELANCE', 0.45
    elif emp == 'Appenticeship':
        return 'APPRENTICE', 0.35
    elif emp == 'Internship':
        return 'INTERN', 0.30
    elif emp == 'Seasonal':
        return 'SEASONAL', 0.40
    else:
        return 'UNKNOWN', 0.10
        
def get_highest_edu_degree_coef(edu_deg):
    if type(edu_deg) == float:
        return 'NO_DEGREE', 0.10
    elif 'PHD' in edu_deg:
        return 'PHD', 1.00
    elif 'MASTERS' in edu_deg:
        return 'MASTERS', 0.75
    elif 'UNDERGRADUATE' in edu_deg:
        return 'UNDERGRADUATE', 0.50
    elif 'ASSOCIATE' in edu_deg:
        return 'ASSOCIATE', 0.35
    elif 'HIGH_SCHOOL' in edu_deg:
        return 'HIGH_SCHOOL', 0.20

def get_edu_degree_major_code(edu):
    edm_code = "";   indices = []
    if type(edu) == float:
        return 'NO_DEGREE', [0]
    edu = edu.lower()
    if 'accounting' in edu:   
        edm_code += "EDM00";    indices.append(0);
    if 'aeronautical' in edu or 'astronautical' in edu:   
        edm_code += " EDM01";   indices.append(1);
    if 'aerospace' in edu:   
        edm_code += " EDM02";   indices.append(2);
    if 'architect' in edu:   
        edm_code += " EDM03";   indices.append(3);
    if 'bachelor of arts' in edu or 'master of arts' in edu:   
        edm_code += " EDM04";   indices.append(4);
    if 'automotive engineering' in edu:   
        edm_code += " EDM05";   indices.append(5);
    if 'biology' in edu or 'biological sciences' in edu:   
        edm_code += " EDM06";   indices.append(6);
    if 'business administration' in edu:   
        edm_code += " EDM07";   indices.append(7);
    if 'business analytics' in edu:   
        edm_code += " EDM08";   indices.append(8);
    if 'business and information system' in edu:   
        edm_code += " EDM09";   indices.append(9);
    if 'chemical engineering' in edu:   
        edm_code += " EDM10";   indices.append(10);
    if 'chemistry' in edu:   
        edm_code += " EDM11";   indices.append(11);
    if 'civil engineering' in edu:   
        edm_code += " EDM12";   indices.append(12);
    if 'community and regional planning' in edu:   
        edm_code += " EDM13";   indices.append(13);
    if 'computer engineering' in edu or 'computer software engineering' in edu:   
        edm_code += " EDM14";   indices.append(14);
    if 'computer information system' in edu:   
        edm_code += " EDM15";   indices.append(15);
    if 'computer network' in edu:   
        edm_code += " EDM16";   indices.append(16);
    if 'computer science' in edu:   
        edm_code += " EDM17";   indices.append(17);
    if 'cybersecurity' in edu or 'cyber security' in edu:   
        edm_code += " EDM18";   indices.append(18);
    if 'data analytics' in edu:   
        edm_code += " EDM19";   indices.append(19);
    if 'data science' in edu:   
        edm_code += " EDM20";   indices.append(20);
    if 'digital media' in edu or 'multimedia' in edu:   
        edm_code += " EDM21";   indices.append(21);
    if 'economics' in edu:   
        edm_code += " EDM22";   indices.append(22);
    if 'electrical and electronics engineering' in edu or 'electronic and information engineering' in edu \
      or 'electronics and communication engineering' in edu or 'electronics and telecommunication' in edu \
      or 'electrical engineering' in edu or 'electrical, electronics and communications engineering' in edu \
      or 'electronics & communications' in edu:   
        edm_code += " EDM23";   indices.append(23);
    if 'entrepreneurship' in edu:   
        edm_code += " EDM24";   indices.append(24);
    if 'environmental engineering' in edu or 'environmental analysis' in edu or 'environmental science' in edu:
        edm_code += " EDM25";   indices.append(25);
    if 'fashion merchandising' in edu:   
        edm_code += " EDM26";   indices.append(26);
    if 'finance' in edu or 'financial' in edu:   
        edm_code += " EDM27";   indices.append(27);
    if 'history' in edu:   
        edm_code += " EDM28";   indices.append(28);
    if 'human computer interaction' in edu:   
        edm_code += " EDM29";   indices.append(29);
    if 'information technology' in edu or 'information engineering technology' in edu or 'information system' in edu \
      or 'information management system' in edu:   
        edm_code += " EDM30";   indices.append(30);
    if 'interior design' in edu:   
        edm_code += " EDM31";   indices.append(31);
    if 'law' in edu:   
        edm_code += " EDM32";   indices.append(32);
    if 'liberal arts' in edu or 'liberal studies' in edu:   
        edm_code += " EDM33";   indices.append(33);
    if 'linguistic' in edu:   
        edm_code += " EDM34";   indices.append(34);
    if 'literature' in edu:   
        edm_code += " EDM35";   indices.append(35);
    if 'machine learning' in edu:   
        edm_code += " EDM36";   indices.append(36);
    if 'marketing' in edu:   
        edm_code += " EDM37";   indices.append(37);
    if 'mathematics' in edu:   
        edm_code += " EDM38";   indices.append(38);
    if 'mechanical engineering' in edu:   
        edm_code += " EDM39";   indices.append(39);
    if 'mechatronics' in edu:   
        edm_code += " EDM40";   indices.append(40);
    if 'medical assistant' in edu or 'medical administration assistant' in edu or 'medical/clinical assistant' in edu:
        edm_code += " EDM41";   indices.append(41);
    if 'nurse' in edu or 'nursing' in edu:   
        edm_code += " EDM42";   indices.append(42);
    if 'operations research' in edu:   
        edm_code += " EDM43";   indices.append(43);
    if 'petroleum engineering' in edu:   
        edm_code += " EDM44";   indices.append(44);
    if 'philosophy' in edu or 'philosofy' in edu:  
        edm_code += " EDM45";   indices.append(45);
    if 'physics' in edu:   
        edm_code += " EDM46";   indices.append(46);
    if 'political science' in edu:   
        edm_code += " EDM47";   indices.append(47);
    if 'psychology' in edu:   
        edm_code += " EDM48";   indices.append(48);
    if 'public health' in edu:   
        edm_code += " EDM49";   indices.append(49);
    if 'radio, television' in edu or 'radio, tv' in edu:   
        edm_code += " EDM50";   indices.append(50);
    if 'radiologic technology' in edu or 'radiographer' in edu:   
        edm_code += " EDM51";   indices.append(51);
    if 'sociology' in edu:   
        edm_code += " EDM52";   indices.append(52);
    if 'software engineering' in edu:   
        edm_code += " EDM53";   indices.append(53);
    if 'statistics' in edu or 'statistical science' in edu:   
        edm_code += " EDM54";   indices.append(54);
    if 'urban planning' in edu or 'urban and regional planning' in edu:   
        edm_code += " EDM55";   indices.append(55);
    if 'web design' in edu:   
        edm_code += " EDM56";   indices.append(56);
    if len(edm_code) == 0:
        edm_code += "UNCT";     indices.append(0);
    return edm_code, indices
    
def get_company_code(company):
    if type(company) == float:
        return 'NO_COMPANY', 0
    company = company.strip()
    if company == 'Amazon':
        return 'CMP00', 0
    elif company == 'Google':
        return 'CMP01', 1
    elif company == 'Oracle':
        return 'CMP02', 2
    elif company == 'Microsoft':
        return 'CMP03', 3
    elif company == 'Apple':
        return 'CMP04', 4
    elif company == 'Meta':
        return 'CMP05', 5
    elif company == 'Cisco':
        return 'CMP06', 6
    elif company == 'Amazon Web Services (AWS)':
        return 'CMP07', 7
    elif company == 'IBM':
        return 'CMP08', 8
    elif company == 'JPMorganChase':
        return 'CMP09', 9
    elif company == 'LinkedIn':
        return 'CMP10', 10
    elif company == 'Capital One':
        return 'CMP11', 11
    elif company == 'Intel Corporation':
        return 'CMP12', 12
    elif company == 'SAIC':
        return 'CMP13', 13
    elif company == 'Tata Consultancy Services':
        return 'CMP14', 14
    elif company == 'Intuit':
        return 'CMP15', 15
    elif company == 'Uber':
        return 'CMP16', 16
    elif company == 'Qualcomm':
        return 'CMP17', 17
    elif company == 'Salesforce':
        return 'CMP18', 18
    elif company == 'Stripe':
        return 'CMP19', 19
    elif company == 'Adobe':
        return 'CMP20', 20
    elif company == 'AECOM':
        return 'CMP21', 21
    elif company == 'NVIDIA':
        return 'CMP22', 22
    elif company == 'PayPal':
        return 'CMP23', 23
    elif company == 'Mastercard':
        return 'CMP24', 24
    elif company == 'Capgemini':
        return 'CMP25', 25
    elif company == 'Walmart':
        return 'CMP26', 26
    elif company == 'HP':
        return 'CMP27', 27
    elif company == 'CGI':
        return 'CMP28', 28
    elif company == 'Tech Mahindra':
        return 'CMP29', 29
    elif company == 'Epic':
        return 'CMP30', 30
    elif company == 'Collins Aerospace':
        return 'CMP31', 31
    elif company == 'Bloomberg':
        return 'CMP32', 32
    elif company == 'U.S. Department of Veterans Affairs':
        return 'CMP33', 33
    elif company == 'BBC':
        return 'CMP34', 34
    elif company == 'Ericsson':
        return 'CMP35', 35
    elif company == 'State Farm':
        return 'CMP36', 36
    elif company == 'Deloitte':
        return 'CMP37', 37
    elif company == 'Tesla':
        return 'CMP38', 38
    elif company == 'Chicago Public Schools':
        return 'CMP39', 39
    elif company == 'HSBC':
        return 'CMP40', 40
    elif company == 'Facebook':
        return 'CMP41', 41
    elif company == 'NYC Department of Education':
        return 'CMP42', 42
    elif company == 'ManTech':
        return 'CMP43', 43
    elif company == 'UniFirst Corporation':
        return 'CMP44', 44
    elif company == 'ATI Physical Therapy':
        return 'CMP45', 45
    elif company == 'Deliveroo':
        return 'CMP46', 46
    elif company == 'Liberty Mutual Insurance':
        return 'CMP47', 47
    elif company == 'Robert Half':
        return 'CMP48', 48
    elif company == 'DaVita Kidney Care':
        return 'CMP49', 49
    elif company == 'Allied Universal':
        return 'CMP50', 50
    elif company == 'Milliman':
        return 'CMP51', 51
    elif company == 'Allstate':
        return 'CMP52', 52
    elif company == 'Angi':
        return 'CMP53', 53
    elif company == 'Vodafone':
        return 'CMP54', 54
    elif company == 'Lloyds Banking Group':
        return 'CMP55', 55
    elif company == 'Fastenal':
        return 'CMP56', 56
    elif company == 'Citi':
        return 'CMP57', 57
    elif company == 'EY':
        return 'CMP58', 58
    elif company == 'Dell Technologies':
        return 'CMP59', 59
    elif company == 'Houlihan Lokey':
        return 'CMP60', 60
    elif company == 'Creative Artists Agency':
        return 'CMP61', 61
    elif company == 'eXp Realty':
        return 'CMP62', 62
    elif company == 'The Home Depot':
        return 'CMP63', 63
    elif company == 'Grand Canyon Education, Inc.':
        return 'CMP64', 64
    elif company == 'Compunnel Inc.':
        return 'CMP65', 65
    elif company == 'US Navy':
        return 'CMP66', 66
    elif company == 'PepsiCo':
        return 'CMP67', 67
    else:
        return 'UNCT', 0
        
def get_main_skills_code(main_skills):
    ms_code = "";   indices = [];
    main_skills = main_skills.split(', ')
    if 'Financial Management' in main_skills:
        ms_code += "MS00";    indices.append(0);
    if 'Python' in main_skills:
        ms_code += " MS01";   indices.append(1);
    if 'Data Engineering' in main_skills:
        ms_code += " MS02";   indices.append(2);
    if 'Microsoft Office' in main_skills:
        ms_code += " MS03";   indices.append(3);
    if 'Programming' in main_skills:
        ms_code += " MS04";   indices.append(4);
    if 'SQL' in main_skills:
        ms_code += " MS05";   indices.append(5);
    if 'SQL Scripting' in main_skills:
        ms_code += " MS06";   indices.append(6);
    if 'Java' in main_skills:
        ms_code += " MS07";   indices.append(7);
    if 'Microsoft Excel' in main_skills:
        ms_code += " MS08";   indices.append(8);
    if 'Leadership' in main_skills:
        ms_code += " MS09";   indices.append(9);
    if 'Data Analysis' in main_skills:
        ms_code += " MS10";   indices.append(10);
    if 'C++' in main_skills:
        ms_code += " MS11";   indices.append(11);
    if 'Marketing Research' in main_skills:
        ms_code += " MS12";   indices.append(12);
    if 'Sales and Marketing' in main_skills:
        ms_code += " MS13";   indices.append(13);
    if 'JavaScript' in main_skills:
        ms_code += " MS14";   indices.append(14);
    if 'Customer Service' in main_skills:
        ms_code += " MS15";   indices.append(15);
    if 'Communication' in main_skills:
        ms_code += " MS16";   indices.append(16);
    if 'HTML' in main_skills:
        ms_code += " MS17";   indices.append(17);
    if 'Project Management' in main_skills:
        ms_code += " MS18";   indices.append(18);
    if 'Research' in main_skills:
        ms_code += " MS19";   indices.append(19);
    if 'C' in main_skills:
        ms_code += " MS20";   indices.append(20);
    if 'PowerPoint' in main_skills:
        ms_code += " MS21";   indices.append(21);
    if 'Machine Learning' in main_skills:
        ms_code += " MS22";   indices.append(22);
    if 'Microsoft Word' in main_skills:
        ms_code += " MS23";   indices.append(23);
    if 'Software Development' in main_skills:
        ms_code += " MS24";   indices.append(24);
    if 'HTML/CSS' in main_skills:
        ms_code += " MS25";   indices.append(25);
    if 'Teamwork' in main_skills:
        ms_code += " MS26";   indices.append(26);
    if 'Public Speaking' in main_skills:
        ms_code += " MS27";   indices.append(27);
    if 'Sales Techniques' in main_skills:
        ms_code += " MS28";   indices.append(28);
    if 'Linux' in main_skills:
        ms_code += " MS29";   indices.append(29);
    if 'Sales Strategy' in main_skills:
        ms_code += " MS30";   indices.append(30);
    if 'Management' in main_skills:
        ms_code += " MS31";   indices.append(31);
    if 'Matlab' in main_skills:
        ms_code += " MS32";   indices.append(32);
    if 'Office Management' in main_skills:
        ms_code += " MS33";   indices.append(33);
    if 'Records Management' in main_skills:
        ms_code += " MS34";   indices.append(34);
    if 'Deadline Management' in main_skills:
        ms_code += " MS35";   indices.append(35);
    if 'CSS' in main_skills:
        ms_code += " MS36";   indices.append(36);
    if 'Marketing' in main_skills:
        ms_code += " MS37";   indices.append(37);
    if 'Visual' in main_skills:
        ms_code += " MS38";   indices.append(38);
    if 'Social Media' in main_skills:
        ms_code += " MS39";   indices.append(39);
    if 'Agile' in main_skills:
        ms_code += " MS40";   indices.append(40);
    if 'Sales' in main_skills:
        ms_code += " MS41";   indices.append(41);
    if 'Testing and Validation' in main_skills:
        ms_code += " MS42";   indices.append(42);
    if 'Testing' in main_skills:
        ms_code += " MS43";   indices.append(43);
    if 'Product Knowledge' in main_skills:
        ms_code += " MS44";   indices.append(44);
    if 'git' in main_skills:
        ms_code += " MS45";   indices.append(45);
    if 'R' in main_skills:
        ms_code += " MS46";   indices.append(46);
    if 'MySQL' in main_skills:
        ms_code += " MS47";   indices.append(47);
    if 'Problem Solving' in main_skills:
        ms_code += " MS48";   indices.append(48);
    if 'Social Media Platforms' in main_skills:
        ms_code += " MS49";   indices.append(49);
    if 'AWS' in main_skills:
        ms_code += " MS50";   indices.append(50);
    if 'Algorithms' in main_skills:
        ms_code += " MS51";   indices.append(51);
    if 'Time Management' in main_skills:
        ms_code += " MS52";   indices.append(52);
    if 'Sales Support' in main_skills:
        ms_code += " MS53";   indices.append(53);
    if 'Computer Networks' in main_skills:
        ms_code += " MS54";   indices.append(54);
    if 'Statistics' in main_skills:
        ms_code += " MS55";   indices.append(55);
    if 'Business Analysis' in main_skills:
        ms_code += " MS56";   indices.append(56);
    if 'Analytical Skills' in main_skills:
        ms_code += " MS57";   indices.append(57);
    if 'Tableau' in main_skills:
        ms_code += " MS58";   indices.append(58);
    if 'Writing' in main_skills:
        ms_code += " MS59";   indices.append(59);
    if 'User Interface Design' in main_skills:
        ms_code += " MS60";   indices.append(60);
    if 'Data Science' in main_skills:
        ms_code += " MS61";   indices.append(61);
    if 'DevOps' in main_skills:
        ms_code += " MS62";   indices.append(62);
    if 'Databases' in main_skills:
        ms_code += " MS63";   indices.append(63);
    if 'Marketing Campaigns' in main_skills:
        ms_code += " MS64";   indices.append(64);
    if 'Web Development' in main_skills:
        ms_code += " MS65";   indices.append(65);
    if 'React' in main_skills:
        ms_code += " MS66";   indices.append(66);
    if 'Marketing Knowledge' in main_skills:
        ms_code += " MS67";   indices.append(67);
    if 'C#' in main_skills:
        ms_code += " MS68";   indices.append(68);
    if 'Data Visualization' in main_skills:
        ms_code += " MS69";   indices.append(69);
    if 'Training' in main_skills:
        ms_code += " MS70";   indices.append(70);
    if 'Object Oriented Programming' in main_skills:
        ms_code += " MS71";   indices.append(71);
    if 'Data Structures' in main_skills:
        ms_code += " MS72";   indices.append(72);
    if 'Data Mining' in main_skills:
        ms_code += " MS73";   indices.append(73);
    if 'Photoshop' in main_skills:
        ms_code += " MS74";   indices.append(74);
    if 'User Experience Design' in main_skills:
        ms_code += " MS75";   indices.append(75);
    if 'Strategic Planning' in main_skills:
        ms_code += " MS76";   indices.append(76);
    if 'Node.js' in main_skills:
        ms_code += " MS77";   indices.append(77);
    if 'Event Planning' in main_skills:
        ms_code += " MS78";   indices.append(78);
    if 'Windows' in main_skills:
        ms_code += " MS79";   indices.append(79);
    if len(ms_code) == 0:
        ms_code = "UNCT";     indices.append(0);
    return ms_code, indices
    