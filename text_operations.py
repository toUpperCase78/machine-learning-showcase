def manipulate_text(text):
    return text.replace('sr. ','senior ').replace('sr ','senior ').replace(' sr ',' senior ') \
        .replace(' sr. ',' senior ').replace('sr.data','senior data') \
        .replace(',','').replace('i̇','i') \
        .replace(' ex ',' ').replace('ex-','').replace('ex - ','') \
        .replace('𝐀𝐦𝐚𝐳𝐨𝐧','amazon').replace('𝐔𝐒𝐂','usc') \
        .replace("we're hiring",'').replace('bellevue wa','bellevue') \
        .replace('aroraakshit.github.io','githubio') \
        .replace('https://www.buildzoom.com/contractor/brend-renovation-corp','buildzoom').replace('j p morgan','jpmorgan') \
        .replace('j.p. morgan','jpmorgan').replace('jp morgan chase','jpmorgan').replace('jp morgan','jpmorgan') \
        .replace('fisker inc','fisker incorporation').replace('us & overseas','usoverseas').replace('2u','toyou') \
        .replace('mental mastery p. a.','mental mastery').replace('p electrical engineer','electrical engineer') \
        .replace('scientist@salesforce','scientist salesforce').replace('cs@northeastern','cs northeastern') \
        .replace('engineer@linkedin','engineer linkedin').replace('engineer@amazon','engineer amazon') \
        .replace('intern@alibaba','intern alibaba').replace('ms.statistics@uiuc','ms statistic uiuc') \
        .replace('engineer@oracle','engineer oracle').replace('scientist@walmart','scientist walmart') \
        .replace('power bi','powerbi').replace('intellij idea','intellijidea').replace('uh alum','alum') \
        .replace('big data','bigdata').replace('beautiful soup','beautifulsoup').replace('capital one','capitalone') \
        .replace('va boston','vaboston').replace('frito lay','fritolay').replace('final cut pro','finalcutpro') \
        .replace('final cut','finalcut').replace('indesign cc','indesigncc') \
        .replace('programme','program').replace('testng','testing').replace('modelling','modeling').replace('plannig','planning') \
        .replace('hardworkig','hardworking').replace('évaluation','evaluation').replace('telemarkting','telemarketing') \
        .replace('anaylisis','analysis') \
        .replace('qa ',' quality assurance ').replace('nbc10','nbcten').replace('dr horton','drhorton') \
        .replace('engineer 2','engineer').replace('developer 3','developer') \
        .replace('cluster(galera','cluster galera').replace('engineer(vulnerability','engineer vulnerability') \
        .replace('system/2(document','systemtwo document') \
        .replace('construction/test/troubleshoot','construction test troubleshoot').replace('player/builder','player builder') \
        .replace('a/b testing','abtesting').replace('ab test','abtesting').replace('illustrator/graphic','illustrator graphic') \
        .replace('manager/program','manager program').replace('c/c++','c cplusplus').replace('java/python','java python') \
        .replace('development/engineer','development engineer').replace('tutoring/teaching','tutoring teaching') \
        .replace('analyst/scientist','analyst scientist').replace('appdynamics/cisco','appdynamics cisco') \
        .replace('proliant/windows/linux','proliant windows linux').replace('data/software','data software') \
        .replace('ml/database','ml database').replace('internals/big','internals big').replace('analyst/network','analyst network') \
        .replace('counselor/certified','counselor certified').replace('practitioner/certified','practitioner certified') \
        .replace('digital/pre-press/packaging','digital prepress packaging').replace('windows/linux','windows linux') \
        .replace('toyou/trilogy','toyou trilogy').replace('uv/vis','uv vis').replace('development/ml','development ml') \
        .replace('docker/ansible/github','docker ansible github').replace('actions/linux','actions linux') \
        .replace('assurance/automation','assurance automation').replace('tester/data','tester data') \
        .replace('learning/computer','learning computer').replace('mohawk/hispanic','mohawk hispanic') \
        .replace('hydrologist/geotechnical/civil','hydrologist geotechnical civil').replace('youtube/google','youtube google') \
        .replace('nursing/careplanning','nursing careplanning').replace('recruitment/retention','recruitment retention') \
        .replace('producer/product','producer product').replace('scientist/subject','scientist subject') \
        .replace('scientist/machine','scientist machine').replace('amazon/imdb','amazon imdb').replace('at&t/ccie','att ccie') \
        .replace('autocad/mathcad/risa/etabs/bluebeam','autocad mathcad risa etabs bluebeam') \
        .replace('tech/boilermaker','tech boilermaker').replace('dietitian/certified','dietitian certified') \
        .replace('medical/clinical','medical clinical').replace('assistant/administrative','assistant administrative') \
        .replace('hardware/software','hardware software').replace('price/promo/markdown','price promo markdown') \
        .replace('civil/structural/transportation','civil structural transportation') \
        .replace('iaas/paas/saas','iaas paas saas').replace('manager/ansible','manager ansible') \
        .replace('git/ci-cd/agile','git cicd agile').replace('campus/fabric/sd-wan','campus fabric sdwan') \
        .replace('administrator/ts-sci','administrator tssci').replace('implementing/managing','implementing managing') \
        .replace('aaa/siem/ids/pki/tacacs+/radius/kerberos','aaa siem ids pki tacacsplus radius kerberos') \
        .replace('ios/asa/juniper','ios asa juniper').replace('snmp/syslog/qos/ntp/tftp','snmp syslog qos ntp tftp') \
        .replace('mode/multi','mode multi').replace('mode)/termination/crimping','mode termination crimping') \
        .replace('rip/ospf/is-is/eigrp/bgp','rip ospf isis eigrp bgp').replace('mpls/gre/ipsec','mpls gre ipsec') \
        .replace('vlan/arp/stp/etherchannel','vlan arp stp etherchannel').replace('hse/hro/scissor','hse hro scissor') \
        .replace('ipv4/ipv6/nat/dns/dhcp','ipvfour ipvsix nat dns dhcp').replace('lift/cherry','lift cherry') \
        .replace('python/javascript/bash/powershell','python javascript bash powershell') \
        .replace('machine/deep','machine deep').replace('excel/vba','excel vba').replace('aix/linux','aix linux') \
        .replace('database/system','database system').replace('physical/logical','physical logical') \
        .replace('products/services','products services').replace('tracing/tkprof','tracing tkprof') \
        .replace('aesthetician/esthetician','aesthetician esthetician').replace('setup/troubleshooting','setup troubleshooting') \
        .replace('oracle/postgresql/mysql','oracle postgresql mysql').replace('awk/sed/grep','awk sed grep') \
        .replace('devops/aws/oracle/mysql/azure','devops aws oracle mysql azure').replace('manager/operations','manager operations') \
        .replace('bartending/serving','bartending serving') \
        .replace('rsqltableauexcelerp/sapetlkpi','r sql tableau excel erp sap etl kpi') \
        .replace('intelligence/machine','intelligence machine').replace('subcontractor/crew','subcontractor crew') \
        .replace('receiver/transmitter','receiver transmitter').replace('python/django','python django') \
        .replace('backup/restore','backup restore').replace('import/export','import export') \
        .replace('spring/hibernate','spring hibernate').replace('compliance/operations','compliance operations') \
        .replace('analyst/engineer','analyst engineer').replace('designer/creative','designer creative') \
        .replace('sd/sdio','sd sdio').replace('spi/i²c/uart','spi isquarec uart').replace('investor/real','investor real') \
        .replace('technologies/certified','technologies certified').replace('hana/sap','hana sap') \
        .replace('bo/qlik/aws/snowflake','bo qlik aws snowflake').replace('embedded/firmware','embedded firmware') \
        .replace('nutritionist/dietitian','nutritionist dietitian').replace('analytical/research','analytical research') \
        .replace('sensitivity/awareness','sensitivity awareness').replace('transfer/few-shot/meta','transfer fewshot meta') \
        .replace('mining/cleansing/modeling/visualization','mining cleansing modeling visualization') \
        .replace('planner/traffic','planner traffic') \
        .replace('athlete||sdr||b2b','athlete sdr btob').replace('sales||saas||tech','sales saas tech') \
        .replace('server|sap|ssis/ssas|etl|tableau|powerbi|teradata|data','server sap siss ssas etl tableau powerbi teradata data') \
        .replace('azure|aws|kubernetes|microservice|ai','azure aws kubernetes microservice ai') \
        .replace('learning|python|iac|automation|containers|cicd','learning python iac automation containers cicd') \
        .replace('nurse|dialysis|home','nurse dialysis home').replace('executive|saas','executive saas') \
        .replace('owner|bookkeeper|payroll','owner bookkeeper payroll').replace('processing|financial','processing financial') \
        .replace('reporting|quickbooks','reporting quickbooks').replace('python|ms','python ms') \
        .replace('engineer|dae@neu','engineer dae neu').replace('persianenglish&dari','persian english dari') \
        .replace('amazon｜product','amazon product') \
        .replace('architectconsultant','architect consultant').replace('hivepigyarn','hive pig yarn') \
        .replace('cisspgctigmongpengcihceh','cissp gcti gmon gpen gcih ceh').replace('pycharmjboss','pycharm jboss') \
        .replace('workstationjmeterfortify','workstation jmeter fortify').replace('scansonar','scan sonar') \
        .replace('electronicdc','electronic dc').replace('electronicconstruction','electronic construction') \
        .replace('gitjenkinsudeploysplunkpostmansoapui','git jenkins udeploy splunk postman soapui') \
        .replace('serversunixlinuxwinscpputtymobaxterm','servers unix linux winscp putty mobaxterm') \
        .replace('studioeclipsespring','studio eclipse spring').replace('rallyjirawebexskype','rally jira webex skype') \
        .replace('developerrobo3ttoadkibana','developer robothreet toad kibana') \
        .replace('pythonsqlsparkgoogle','python sql spark google').replace('cloudlooker','cloud looker') \
        .replace('googlecloudcertified','google cloud certified').replace('systempmp','system pmp') \
        .replace('java/j2eepythonmicroservicespivotal','java jtwoee python microservices pivotal') \
        .replace('foundryspringsql','foundry spring sql').replace('ericssoncalifornia','ericsson california') \
        .replace('inc.','incorporation').replace('co.','company') \
        .replace('salesforce.org','salesforce').replace('sales force','salesforce').replace('first aid','firstaid') \
        .replace('black box','blackbox').replace('white box','whitebox') \
        .replace('front-end','frontend').replace('front end','frontend').replace('p and l','pandl') \
        .replace('back-end','backend').replace('back end','backend').replace('ruby on rails','rubyonrails') \
        .replace('voice over ip','voiceoverip').replace('internet of things','internetofthings') \
        .replace('javaserver pages','javaserverpages').replace('java server pages','javaserverpages') \
        .replace('go-to-market','market') \
        .replace('parent-teacher','parent teacher').replace('spanish-speaking','spanish speaking') \
        .replace('gardaworld-site','gardaworld site').replace('singer-songwriter','singer songwriter') \
        .replace('walmart-labs','walmart labs').replace('president-icm','president icm') \
        .replace('certification-hardware','certification hardware').replace('sagemaker-groundtruth','sagemaker groundtruth') \
        .replace('model-view-controller','modelviewcontroller').replace('cost-effective','costeffective') \
        .replace('object-oriented','objectoriented').replace('service-oriented','serviceoriented') \
        .replace('field-programmable','field programmable').replace('user-centered','usercentered') \
        .replace('cross-functional','crossfunctional').replace('behavior-driven','behaviordriven') \
        .replace('very-large-scale','verylargescale').replace('random-access','randomaccess') \
        .replace('cyber-physical','cyberphysical').replace('application-specific','applicationspecific') \
        .replace('time-efficient','timeefficient').replace('cloud-native','cloudnative') \
        .replace('executive-level','executivelevel').replace('domain-driven','domaindriven') \
        .replace('decision-making','decisionmaking').replace('medical-surgical','medicalsurgical') \
        .replace('test-driven','testdriven') \
        .replace('chick-fil-a-franchise','chickfila franchise') \
        .replace('grc/irm-secops','grc irm secops') \
        .replace('meta(whatsapp)','meta whatsapp').replace('pi(python)','pi python').replace('oracle(oci)','oracle oci') \
        .replace('iit(bhu)','iit bhu').replace('interpretation(english/chinese)','interpretation english chinese') \
        .replace('ruby on rails','ruby rails').replace('system on chip','system chip') \
        .replace('info sec','info').replace('test‚äìdriven','test ai driven') \
        .replace('u.s.','united states').replace('.com','') \
        .replace('.js','js').replace('t-sql','tsql').replace('pl/sql','plsql') \
        .replace('tcp/ip','tcpip').replace('ui/ux','uiux').replace('ci/cd','cicd').replace('ar/vr','arvr') \
        .replace('bi/data','bi data').replace('ai/ml','ai ml').replace('analyst/data','analyst data') \
        .replace('html/css','html css').replace('wifi 6/6e','wifi').replace('cad/cam','cad cam') \
        .replace('python/c/c++','python c cplusplus').replace('java/j2ee','java jtwoee') \
        .replace('.net','dotnet').replace('c++','cplusplus').replace('c#','csharp').replace('brf+','brfplus') \
        .replace('sql*net/net','sqlnet').replace('sql*plus','sqlplus').replace('sql*loader','sqlloader') \
        .replace('l2/l3','l2 l3').replace('p&l','profit loss').replace('apis','api') \
        .replace('gd&t','geometric dimensioning tolerancing').replace('d&o','directors officers') \
        .replace('r&d','research development').replace('v&v','verification validation') \
        .replace('m&a','mergers acquisitions') \
        .replace('exam fm','examfm').replace('exam p','examp').replace(' p spice',' pspice') \
        .replace('html 5','html').replace('html5','html').replace('web 2.0','web') \
        .replace('unity3d','unity 3d').replace('cocos2d','cocostwod') \
        .replace('angular 2','angular').replace('python 3','python') \
        .replace('windows 7','windows').replace('windows 8.1','windows').replace('windows 10','windows') \
        .replace('windows xp','windows').replace('microsoft 365','microsoft').replace('office 365','office') \
        .replace('mac os x','macos').replace('mac os','macos').replace('os x','macos') \
        .replace('vs code','visual studio code').replace('m code','mcode').replace('matlap','matlab') \
        .replace('1st','first').replace('2nd','second').replace('3rd','third').replace('4th','fourth') \
        .replace('2d','twodimension').replace('3d','threedimension').replace('4d','fourdimension') \
        .replace('3g','threeg').replace('4g','fourg').replace('5g','fiveg') \
        .replace('b2b','btob').replace('h.264','htwosixfour').replace('ec2','ectwo').replace('s3','sthree') \
        .replace('db2','dbtwo').replace('hl7','hlseven').replace('ipv4','ipvfour').replace('ipv6','ipvsix') \
        .replace('j2ee','jtwoee').replace('5s','fives').replace('3m','threem').replace('m3','mthree') \
        .replace('ss7','ssseven').replace('robo3t','robothreet').replace('mpeg-4','mpegfour').replace('mpeg4','mpegfour') \
        .replace('mpeg-2','mpegtwo').replace('mpeg2','mpegtwo').replace('m5','mfive').replace('l10n','ltenn') \
        .replace('rg6','rgsix').replace('a+','aplus').replace('a +','aplus').replace('r/3','rthree') \
        .replace('p4','pfour').replace('p6','psix').replace('p/1','pone').replace('fm/2','fmtwo') \
        .replace('x86_64','xeightysixsixtyfour').replace('x86','xeightysix').replace('mfe/3f','mfethreef') \
        .replace('s/4hana','sfourhana') \
        .replace('2x','').replace('2 x','').replace('hold 3','').replace('2400v','').replace('15kv','').replace('10g/11g','') \
        .replace('401k','').replace('sap2000','sap').replace('2005/2000','').replace('2000-2008','').replace('10-hour','') \
        .replace('m1','').replace('k-12','').replace('13c','').replace('11g','') \
        .replace('4.0','').replace('5.0','').replace("'23",'').replace("'21",'').replace('7+','').replace('#1','') \
        .replace('1','').replace('2','').replace('3','').replace('4','').replace('5','') \
        .replace('6','').replace('7','').replace('8','').replace('9','').replace('0','') \
        .replace(' my ',' ').replace(' him ',' ').replace(' her ',' ').replace(' with ',' ').replace(' from ',' ') \
        .replace(' are ',' ').replace(' who ',' ').replace(' for ',' ').replace(' the ',' ').replace(' and ',' ') \
        .replace(' in ', ' ').replace(' of ',' ').replace(' to ',' ').replace(' under ',' ') \
        .replace(' i ', ' ').replace(' ii ',' ').replace(' iii ',' ').replace(' l ',' ').replace(' ll ',' ') \
        .replace(' at ',' ').replace(' as ',' ').replace(' on ',' ').replace(' a ',' ').replace(' an ',' ') \
        .replace(' ww ',' ') \
        .replace('.','').replace(';','').replace('#','').replace('+','').replace('/','').replace('\\','') \
        .replace("'",'').replace('"','').replace('-','').replace('–','').replace('—','').replace('=','') \
        .replace('|','').replace('&','').replace('‘','').replace(':','').replace('®','').replace('!','') \
        .replace('?','').replace('_','').replace('’','').replace('“','').replace('”','').replace('@','') \
        .replace('(','').replace(')','').replace('[','').replace(']','').replace('{','').replace('}','') \
        .replace('•','').replace('┃','').replace('♦','').replace('★','').replace('｜','').replace('▪️','') \
        .replace('♣','').replace('➤','').replace('⚙','').replace('™','') \
        .replace('☁','').replace('	','') \
        .replace('\uf8ff','').replace('🖼','').replace('🏘','') \
        .replace('☁️','').replace('📈','').replace('📊','').replace('🎨','').replace('💵','').replace('✨','') \
        .replace('🐝','').replace('🎯','').replace('🪖','').replace('🔜','').replace('💻','').replace('🦘','').replace('👨🏾‍','') \
        .replace('😊','').replace('👇','').replace('🏠','').replace('🟠','').replace('⚪️','').replace('🐾','').replace('🌐','') \
        .replace('✏️','').replace('💖','').replace('🫶🏾','').replace('👨‍🎓','').replace('📍','').replace('🏆','').replace('🥰','') \
        .replace('💡','').replace('❤️','').replace('💼','').replace('🎙️','').replace('🤝','').replace('👩🏽‍🎓','').replace('🎉','') \
        .replace('🔎','').replace('🤖','').replace('⚙️','').replace('🎟️','').replace('🏳️‍🌈','').replace('🪴','').replace('📉','') \
        .replace('⚡️','').replace('✍️','').replace('🤸🏽','').replace('📢','').replace('👨🏻‍','').replace('🍎','').replace('🎮','') \
        .replace('🧑🏻‍','').replace('🪬','').replace('🚀','').replace('™️','').replace('🚗','').replace('🧠','').replace('🏀','') \
        .replace('💰','').replace('🌎','').replace('⭐','').replace('🎓','').replace('💁','').replace('💊','').replace('🔍','') \
        .replace('📲','').replace('👩‍','').replace('🧡','').replace('🚨','').replace('🔋','') \
        .replace(' 🏿','').replace('   ',' ').replace('  ',' ').strip()
		
### Languages included: Turkish, Spanish, Portuguese, German, French, Dutch, Russian, Polish, Chinese, Korean, Indian
def translate_to_english(text):
    return text.replace('optimisation','optimization') \
        .replace('yetenek olgunluk model entegrasyonu','capability maturity model integration') \
        .replace('nesne yönelimli programlama','object oriented programming') \
        .replace('topluluk önünde konuşma','public speaking') \
        .replace('yapay sinir ağları','artificial neural networks') \
        .replace('işletim sistemleri','operating systems') \
        .replace('nesnelerin interneti','internetofthings') \
        .replace('proje yönetimi','project management') \
        .replace('programlama dilleri','programming languages') \
        .replace('matematik modelleme','mathematical modeling') \
        .replace('tasarımcı düşünce','designer thinking') \
        .replace('analitik beceriler','analytical skills') \
        .replace('endüstriyel tasarım','industrial design') \
        .replace('kavramsal tasarım','conceptual design') \
        .replace('makine öğrenimi','machine learning') \
        .replace('müşteri hizmetleri','customer service') \
        .replace('öğrenme yetenekleri','learning abilities') \
        .replace('piyasa araştırması','market research') \
        .replace('tasarım örüntüleri','design patterns') \
        .replace('assembly dili','assembly language') \
        .replace('ürün geliştirme','product development') \
        .replace('ürün tasarımı','product design') \
        .replace('yedekleme planlaması','backup planning') \
        .replace('veritabanı geliştirme','database development') \
        .replace('veri yapıları','data structures') \
        .replace('veri bilimi','data science') \
        .replace('veri analizi','data analysis') \
        .replace('agile metotları','agile methods') \
        .replace('yabancı diller','foreign languages') \
        .replace('yapay zeka','artificial intelligence') \
        .replace('yazılım tasarımı','software design') \
        .replace('ekip çalışması','teamwork') \
        .replace('gıda güvenliği','food safety') \
        .replace('yiyecek endüstrisi','food industry') \
        .replace('yiyecek hazırlama','food preparation') \
        .replace('doğrudan satış','direct sales') \
        .replace('algoritmalar','algorithms') \
        .replace('geliştirme','development') \
        .replace('programlama','programming') \
        .replace('araştırma','research') \
        .replace('yazılım','software') \
        .replace('ingilizce','english') \
        .replace('eğitim','education') \
        .replace('kahve','coffee') \
        .replace('kasiyer','cashier') \
        .replace('satış','sales') \
        .replace('conjunto de datos e información sobre la eficacia de la atención médica',
                 'data information set health care effectiveness') \
        .replace('setor de produção de petróleo e gás natural','oil natural gas production sector') \
        .replace('administración y dirección de empresas','business administration management') \
        .replace('aptitudes de laboratorio','laboratory skills') \
        .replace('conocimientos informáticos','computer skills') \
        .replace('arquitectura informática','computer architecture') \
        .replace('depuración de programas','program debugging') \
        .replace('desarrollo de productos','product development') \
        .replace('estratégia empresarial','business strategy') \
        .replace('gestión de proyectos','project management') \
        .replace('razonamiento deductivo','deductive reasoning') \
        .replace('instrumentación electrónica','electronic instrumentation') \
        .replace('lanzamiento de productos','product launch') \
        .replace('planificación estratégica','strategic planning') \
        .replace('procesamiento de señales','signal processing') \
        .replace('pruebas de validación','validation test') \
        .replace('validación y verificación','validation verification') \
        .replace('reanimación cardiopulmonar','cardiopulmonary resuscitation') \
        .replace('venta farmacéutica','pharmaceutical sales') \
        .replace('programación de citas','appointment scheduling') \
        .replace('soporte vital básico','basic life support') \
        .replace('educación del paciente','patient education') \
        .replace('automação de testes','test automation') \
        .replace('cuidado de pacientes','patient care') \
        .replace('evaluación de pacientes','patient evaluation') \
        .replace('extracciones de sangre','blood draw') \
        .replace('glucosa en sangre','blood glucose') \
        .replace('presión sanguínea','blood pressure') \
        .replace('medicina intensiva','intensive medicine') \
        .replace('control de infecciones','infection control') \
        .replace('enfermedades infecciosas','infectious diseases') \
        .replace('pruebas de función pulmonar','pulmonary function tests') \
        .replace('flujo de pacientes','patient flow') \
        .replace('historia clínica','medical record') \
        .replace('soporte vital','life support') \
        .replace('computación en la nube','cloud computing') \
        .replace('servicio de atención al cliente','customer service') \
        .replace('design da experiência do usuário','user experience design') \
        .replace('operaciones de redes informáticas','computer network operations') \
        .replace('gestión de relaciones con clientes','customer relationship management') \
        .replace('planificación de recursos empresariales','enterprise resource planning') \
        .replace('creación de oportunidades de negocio','creating business opportunities') \
        .replace('procesamiento de grandes volúmenes de datos','big data processing') \
        .replace('investigación y desarrollo','research development') \
        .replace('infraestructura de red','network infrastructure') \
        .replace('industria farmacéutica','pharmaceutical industry') \
        .replace('asistencia médica','medical assistance') \
        .replace('asistencia domicilio','home care') \
        .replace('cuidados intensivos','intensive care') \
        .replace('ingeniería de redes','network engineering') \
        .replace('minería de datos','data mining') \
        .replace('inteligência empresarial','business intelligence') \
        .replace('visualización de datos','data visualization') \
        .replace('capacidad de análisis','analysis capacity') \
        .replace('capacidad de respuesta','responsiveness') \
        .replace('análisis de requisitos','requirements analysis') \
        .replace('análisis de orina','urine analysis') \
        .replace('análisis de datos','data analysis') \
        .replace('ciencia de datos','data science') \
        .replace('aprendizaje automático','machine learning') \
        .replace('modelos matemáticos','mathematical models') \
        .replace('experiencia del cliente','customer experience') \
        .replace('eficacia de ventas','sales effectiveness') \
        .replace('makeup applicatior','makeup application') \
        .replace('control de proyectos','project control') \
        .replace('inglês fluente','fluent english') \
        .replace('industria petrolera','oil industry') \
        .replace('visual análisis de datos','visual data analysis') \
        .replace('ingeniería del petróleo','petroleum engineering') \
        .replace('instalación de software','software installation') \
        .replace('inteligencia artificial','artificial intelligence') \
        .replace('servicio de atención al cliente','customer service') \
        .replace('aptitudes de organización','organizational skills') \
        .replace('servidores de seguridad','security servers') \
        .replace('atendimento ao cliente','customer service') \
        .replace('atendimento ao paciente','patient service') \
        .replace('asistencia sanitaria','health care') \
        .replace('captação de clientes','customer acquisition') \
        .replace('recogida de especímenes','specimen collection') \
        .replace('definição de metas','definition goals') \
        .replace('gestão de projetos','project management') \
        .replace('gestão de conflitos','conflict management') \
        .replace('gestão de vendas','sales management') \
        .replace('gestión de redes sociales','social media management') \
        .replace('gestión de medios line','online media management') \
        .replace('gestión de redes','network management') \
        .replace('gestión operativa','operational management') \
        .replace('gestion de projet','project management') \
        .replace('gestión de proyectos','project management') \
        .replace('habilidades sociales','social skills') \
        .replace('planeamiento de proyectos','project planning') \
        .replace('desarrollo de proyectos','project development') \
        .replace('desarrollo de software','software development') \
        .replace('mejora continua','continuous improvement') \
        .replace('marketing de mídias sociais','social media marketing') \
        .replace('resolução de problemas','problem solving') \
        .replace('autorización previa','prior authorization') \
        .replace('atención telefónica','telephone assistance') \
        .replace('diseño de redes','network design') \
        .replace('diseño de moda','fashion design') \
        .replace('arte y manualidades','arts crafts') \
        .replace('industria cosmética','cosmetic industry') \
        .replace('trabalho em equipe','teamwork') \
        .replace('trabajo en equipo','teamwork') \
        .replace('espíritu de equipo','team spirit') \
        .replace('relación con el cliente','customer relationship') \
        .replace('solución de problemas','troubleshooting') \
        .replace('relaciones laborales','labor relations') \
        .replace('orientación objetivos','goal orientation') \
        .replace('optimización de procesos','process optimization') \
        .replace('comunicación inalámbrica','wireless communication') \
        .replace('asistencia directa al paciente','direct patient care') \
        .replace('publicidad en las redes sociales','advertising social networks') \
        .replace('eficacia organizacional','organizational effectiveness') \
        .replace('desenvolvimento de negócios','business development') \
        .replace('desenvolvimento de novos negócios','new business development') \
        .replace('desenvolvimento de software','software development') \
        .replace('desenvolvimento android','android development') \
        .replace('desenvolvimento de jogos eletrônicos','video game development') \
        .replace('desenvolvimento de backend','backend development') \
        .replace('unix aplicativos web','unix web applications') \
        .replace('linguagem de programação','programming language') \
        .replace('protocolos de internet','internet protocol') \
        .replace('redes informáticas','computer networks') \
        .replace('soporte técnico','technical support') \
        .replace('computação gráfica','computer graphics') \
        .replace('engenharia de software','software engineering') \
        .replace('requisitos de software','software requirements') \
        .replace('gestión de compras','purchasing management') \
        .replace('sector automovilístico','automotive sector') \
        .replace('procedimientos de oficina','office procedures') \
        .replace('manutenção preventiva','preventive maintenance') \
        .replace('asesoramiento académico','academic counseling') \
        .replace('planejamento de projetos','project planning') \
        .replace('páginas de visualforce','visualforce pages') \
        .replace('perfuração ao largo','offshore drilling') \
        .replace('sistemas embebidos','embedded systems') \
        .replace('espíritu empresarial','entrepreneurship') \
        .replace('pedidos de compra','purchase orders') \
        .replace('redes sociales','social networks') \
        .replace('maquillador','makeup artist') \
        .replace('electrónica','electronic') \
        .replace('liderazgo','leadership') \
        .replace('manufactura','manufacture') \
        .replace('pruebas','validation') \
        .replace('docência','teaching') \
        .replace('español','spanish') \
        .replace('inglês','english') \
        .replace('cardiologia','cardiology') \
        .replace('requisiciones','requisitions') \
        .replace('comunicação','communication') \
        .replace('comunicación','communication') \
        .replace('liderança','leadership') \
        .replace('presupuestos','budgets') \
        .replace('microcontroladores','microcontrollers') \
        .replace('empreendedorismo','entrepreneurship') \
        .replace('confidencialidad','confidentiality') \
        .replace('contabilidad','accounting') \
        .replace('recomendaciones','recommendations') \
        .replace('programación','programming') \
        .replace('fisioterapia','physiotherapy') \
        .replace('publicidad','advertising') \
        .replace('creatividad','creativity') \
        .replace('conmutadores','switches') \
        .replace('enrutadores','routers') \
        .replace('enrutamiento','routing') \
        .replace('microondas','microwave') \
        .replace('operaciones','operations') \
        .replace('espirometría','spirometry') \
        .replace('seguimiento','tracing') \
        .replace('estratégia','strategy') \
        .replace('formación','formation') \
        .replace('delegación','delegation') \
        .replace('calibração','calibration') \
        .replace('oratoria','oratory') \
        .replace('análisis','analysis') \
        .replace('compras','shopping') \
        .replace('mecanografia','typing') \
        .replace('redacción','drafting') \
        .replace('entrevistas','interviews') \
        .replace('negociación','negotiation') \
        .replace('inmunizaciones','immunizations') \
        .replace('mentoria','mentoring') \
        .replace('diseño','design') \
        .replace('ventas','sales') \
        .replace('inyecciones','injections') \
        .replace('clínicas','clinics') \
        .replace('triaje','triage') \
        .replace('vacunas','vaccines') \
        .replace('flebotomía','phlebotomy') \
        .replace('terminología','terminology') \
        .replace('hospitales','hospitals') \
        .replace('telecomunicaciones','telecommunications') \
        .replace('programmiersprache','programming language') \
        .replace('datenstrukturen','data structures') \
        .replace('softwareentwicklung','software development') \
        .replace('vrentwicklung','vr development') \
        .replace('algorithmens','algorithms') \
        .replace('bigdata et informatique décisionnelle','big data business intelligence') \
        .replace('régressions econométriques et analyse des données sur','economic regressions data analysis') \
        .replace('gestion de la relation avec les fournisseurs','supplier relationship management') \
        .replace('gestion de bases de données sur sql','database management sql') \
        .replace('développement pour android','development android') \
        .replace('gestion de risques','risk management') \
        .replace('apprentissage automatique','machine learning') \
        .replace('intelligence artificielle','artificial intelligence') \
        .replace('segmentation clientèle','customer segmentation') \
        .replace('reporting et performance sur','reporting performance') \
        .replace('réglémentations bancaires','banking regulations') \
        .replace('produits dérivés et pricing','derivatives pricing') \
        .replace('développement de logiciel','software development') \
        .replace('amélioration des processus','process improvement') \
        .replace('procesos de compra','purchasing process') \
        .replace('conception assistée par ordinateur','computeraided design') \
        .replace('mathématiques financières','financial mathematics') \
        .replace('génie mécanique','mechanical engineering') \
        .replace('méthode des éléments finis','finite element method') \
        .replace('budgétisation et prévision','budgeting forecasting') \
        .replace('résolution de problèmes','problem solving') \
        .replace('étude de marché','market research') \
        .replace('stratégie marketing','marketing strategy') \
        .replace('parler en public','public speaking') \
        .replace('travail déquipe','teamwork') \
        .replace('bâle à bâle','basel basel') \
        .replace('français','french') \
        .replace('programmation','programming') \
        .replace('planification','planning') \
        .replace('portfoliomanagement','portfolio management') \
        .replace('oplossen van problemen','troubleshooting') \
        .replace('financiële analyse','financial analysis') \
        .replace('financiële markten','financial market') \
        .replace('financiën','finance') \
        .replace('investeringen','investment') \
        .replace('ondernemerschap','entrepreneurship') \
        .replace('statistieken','statistics') \
        .replace('problemlösning','problem solving') \
        .replace('профессиональные навыки работы с компьютером','professional computer skills') \
        .replace('брокерская деятельность в области страховых услуг','brokerage activities insurance services') \
        .replace('работа с кредиторской задолженностью','work payable accounts') \
        .replace('гибкая методология программирования','agile programming methodology') \
        .replace('разработка мобильных приложений','mobile application development') \
        .replace('разработка приложений для','application development') \
        .replace('разработка программного обеспечения','software development') \
        .replace('управление предприятием','enterprise management') \
        .replace('финансовая отчётность','financial statements') \
        .replace('поиск и устранение неисправностей','troubleshooting') \
        .replace('промышленное производство','industrial production') \
        .replace('техническая документация','technical documentation') \
        .replace('непрерывная интеграция','continuous integration') \
        .replace('отношения с клиентами','customer relations') \
        .replace('управление проектами','project management') \
        .replace('критическое мышление','critical thinking') \
        .replace('машинное обучение','machine learning') \
        .replace('наука о данных','data science') \
        .replace('научная деятельность','scientific activity') \
        .replace('искусственный интеллект','artificial intelligence') \
        .replace('обработка изображений','image processing') \
        .replace('рекомендательные системы','recommendation system') \
        .replace('аналитические навыки','analytical skills') \
        .replace('английский язык','english language') \
        .replace('письменное сообщение','written message') \
        .replace('сбор данных','data collection') \
        .replace('структуры данных','data structures') \
        .replace('финансовый анализ','financial analysis') \
        .replace('финансовое моделирование','financial modeling') \
        .replace('фотографическое искусство','photographic art') \
        .replace('межличностное общение','interpersonal communication') \
        .replace('выверка счетов','account reconciliation') \
        .replace('заказы на  поставку','supply orders') \
        .replace('заказы на поставку','supply orders') \
        .replace('общее страхование','general insurance') \
        .replace('решение задач','problem solving') \
        .replace('сводные таблицы','pivot tables') \
        .replace('страхование жилища','home insurance') \
        .replace('страхование транспортных средств','vehicle insurance') \
        .replace('страхование от несчастных случаев','accident insurance') \
        .replace('конструктивная критика','constructive criticism') \
        .replace('страховые полисы','insurance policies') \
        .replace('контроль качества','quality control') \
        .replace('обслуживание клиентов','customer service') \
        .replace('венчурный капитал','venture capital') \
        .replace('корпоративные финансы','corporate finance') \
        .replace('частное инвестирование','private investment') \
        .replace('шаблоны проектирования','design patterns') \
        .replace('страхование','insurance') \
        .replace('финансы','finance') \
        .replace('электронные таблицы','spreadsheets') \
        .replace('инженерное дело','engineering') \
        .replace('аудит','audit') \
        .replace('продажи','sales') \
        .replace('скрам','scrum') \
        .replace('строительство','construction') \
        .replace('разработка по','development') \
        .replace('бухгалтерский учёт','accounting') \
        .replace('командная работа','teamwork') \
        .replace('розничная торговля','retail') \
        .replace('стратегия','strategy') \
        .replace('физика','physics') \
        .replace('алгоритмы','algorithms') \
        .replace('eksploracja danych','data mining') \
        .replace('procedury przechowywane','stored procedures') \
        .replace('rozwiązywanie problemów','problem solving') \
        .replace('umiejętności analityczne','analytical skills') \
        .replace('komunikacja','communication') \
        .replace('szczegółowość','detail') \
        .replace('统计数据分析','statistical data analysis') \
        .replace('趨勢科技','trending technology') \
        .replace('在线调研','online research') \
        .replace('無線網路','wireless network') \
        .replace('疑難排解','troubleshooting') \
        .replace('網路電話','internet telephone') \
        .replace('網際網路協定套組','internet protocol suite') \
        .replace('網際網路通訊協定','internet protocol') \
        .replace('公开演讲','public speaking') \
        .replace('數位媒體','digital media') \
        .replace('客戶關係管理','customer relationship management') \
        .replace('幾何尺寸與公差','geometric dimensions tolerances') \
        .replace('应用程序开发','application development') \
        .replace('智能软件','intelligent software') \
        .replace('社群媒體行銷','social media marketing') \
        .replace('有限元素分析','finite element analysis') \
        .replace('亚马逊网络服务系统','amazon web services') \
        .replace('实验室技能','laboratory skills') \
        .replace('团队建设','team building') \
        .replace('外語','foreign language') \
        .replace('人工智能','artificial intelligence') \
        .replace('人工智慧','artificial intelligence') \
        .replace('機器學習','machine learning') \
        .replace('机器学习','machine learning') \
        .replace('雙語溝通','bilingual communication') \
        .replace('演讲技能','presentation skills') \
        .replace('应用程序开发','application development') \
        .replace('分析技能','analytical skills') \
        .replace('计划管理','program management') \
        .replace('管理人员','management personnel') \
        .replace('个人发展','personal development') \
        .replace('产品管理','product management') \
        .replace('產品管理','product management') \
        .replace('项目管理','project management') \
        .replace('项目规划','project planning') \
        .replace('科研管理','research management') \
        .replace('数据结构','data structure') \
        .replace('数据分析','data analysis') \
        .replace('資料科學','data science') \
        .replace('社群媒體','social media') \
        .replace('社交媒体','social media') \
        .replace('金融建模','financial modeling') \
        .replace('產品設計','product design') \
        .replace('影像處理','image processing') \
        .replace('電腦視覺','computer vision') \
        .replace('智能软件','intelligent software') \
        .replace('人像摄影','portrait photography') \
        .replace('风险管理','risk management') \
        .replace('使用者體驗設計','user experience design') \
        .replace('用戶體驗','user experience') \
        .replace('实验性研究','experimental studies') \
        .replace('機械工程','mechanical engineering') \
        .replace('计量经济学','econometrics') \
        .replace('數位行銷','digital marketing') \
        .replace('云端平台','cloud platform') \
        .replace('领导力','leadership') \
        .replace('团队合作','teamwork') \
        .replace('英语','english') \
        .replace('研究','research') \
        .replace('药剂学','pharmacy') \
        .replace('软件','software') \
        .replace('医药','medicine') \
        .replace('生物','biology') \
        .replace('編輯','edit') \
        .replace('行銷','marketing') \
        .replace('演算法','algorithm') \
        .replace('算法','algorithm') \
        .replace('数据库','database') \
        .replace('程式設計','programming') \
        .replace('廣告','advertisement') \
        .replace('爱立信','ericsson') \
        .replace('沃尔玛','walmart') \
        .replace('英文','english') \
        .replace('语言','language') \
        .replace('摄影','photography') \
        .replace('工程','engineering') \
        .replace('機器人','robot') \
        .replace('设计','design') \
        .replace('통합팀관리','integrated team management') \
        .replace('리스크관리','risk management') \
        .replace('크리에이티브','creativity') \
        .replace('데이터입력','data entry') \
        .replace('문제해결','problem solving') \
        .replace('데이터분석','data analysis') \
        .replace('미디어기획','media planning') \
        .replace('사업개발','business development') \
        .replace('사업전략','business strategy') \
        .replace('소셜미디어','social media') \
        .replace('전략기획','strategic planning') \
        .replace('재무분석','financial analysis') \
        .replace('금융모델','financial modeling') \
        .replace('제품개발','product development') \
        .replace('재무감사','financial audit') \
        .replace('고객서비스','customer service') \
        .replace('팀워크','teamwork') \
        .replace('비즈니스','business') \
        .replace('오피스','office') \
        .replace('제조','manufacturing') \
        .replace('리더십','leadership') \
        .replace('예측','prediction') \
        .replace('한국어','korean') \
        .replace('영어','english') \
        .replace('온라인','online') \
        .replace('회계','accounting') \
        .replace('인터넷','internet') \
        .replace('광고','advertisement') \
        .replace('디지털','digital') \
        .replace('마케팅','marketing') \
        .replace('프로젝트','project') \
        .replace('재무','finance') \
        .replace('관리','management') \
        .replace('연설','speech') \
        .replace('감사','thanks') \
        .replace('소통','communication') \
        .replace('분석','analysis') \
        .replace('연금','pension') \
        .replace('통계','statistics') \
        .replace('अक्षित','akshit') \
        .replace('अरोड़ा','arora')