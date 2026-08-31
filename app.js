const translations = {
    en: {
        pageTitle: 'Korakod Phongdee | Software Engineer',
        headline: 'Software Engineer | C++ / .NET | Automation Engineer',
        contact: 'Contact',
        bangkok: 'Bangkok, Thailand',
        samutprakarn: 'Samutprakarn, Thailand',
        chonburi: 'Chonburi, Thailand',
        profile: 'Profile',
        profileText: '.NET full-stack developer with software and hardware backgrounds spanning web and desktop applications, REST APIs, embedded systems, IoT, and industrial protocol integration. Experienced in insurance technology, industrial label printing, RFID solutions, rail signaling simulators, and industrial IoT.',
        education: 'Education',
        bachelor: 'Bachelor Degree in Engineering Mechatronics',
        mut: 'Mahanakorn University of Technology',
        highVocational: 'High Vocational Certificate in Technology Computer Hardware',
        vocational: 'Vocational Certificate in Electronics',
        etech: 'Eastern Technological College E-TECH',
        skills: 'Skills',
        skillFrontend: '<b>Frontend:</b> HTML, CSS3, JavaScript, jQuery, Bootstrap, React',
        skillBackend: '<b>Backend:</b> C# (.NET Framework, .NET Core), C++, Python, Lua, Node.js',
        skillDatabase: '<b>Database:</b> Microsoft SQL Server, PostgreSQL, MySQL',
        skillApi: '<b>API &amp; Integration:</b> RESTful APIs, AEP, RFID systems',
        skillIot: '<b>Embedded / IoT:</b> Arduino, Raspberry Pi, Node-RED, Linux',
        skillProtocols: '<b>Industrial protocols:</b> RS232, RS485, Modbus, LoRaWAN',
        skillEngineering: '<b>Engineering:</b> SolidWorks, engineering drawing, basic electronics',
        languages: 'Languages',
        thaiLanguage: '<b>Thai:</b> Native',
        englishLanguage: '<b>English:</b> TOEIC 850 (2023)',
        workExperience: 'Work Experience',
        tbrokerRole: 'Software Developer - Assistant Manager, Business Analyst',
        tbrokerDates: 'Mar 2025 - May 2026',
        tbroker1: "Developed and maintained a web application supporting agents' sales operations.",
        tbroker2: 'Developed and maintained REST APIs integrated with external platforms, including LINE Chatbot and Core Systems.',
        tbroker3: 'Performed SIT and UAT testing to prevent software malfunctions before release.',
        tbroker4: 'Collaborated with an external penetration testing vendor to identify and resolve web application security vulnerabilities.',
        tbroker5: 'Planned and estimated development time and resources based on business requirements.',
        tbroker6: 'Provided technical support and troubleshooting for agents and end users.',
        satoRole: 'Software Developer - Customer Service',
        satoDates: 'Jan 2024 - Feb 2025',
        sato1: 'Developed .NET web applications supporting a Label Printing System and RFID solutions.',
        sato2: 'Built AEP applications enabling stand-alone printing on SATO printers.',
        sato3: 'Delivered tailor-made software solutions based on individual customer requirements.',
        sato4: 'Provided on-site installation and on-site/remote troubleshooting support.',
        sato5: 'Produced project documentation, including user manuals, system diagrams, man-day estimates, and wireframe demos.',
        dtcRole: 'Engineer - Research & Development (Hardware IoT)',
        dtcDates: 'Jul 2023 - Sep 2023',
        dtc1: 'Evaluated and tested sensors and hardware devices in real-world applications.',
        dtc2: 'Developed embedded firmware and data processing pipelines for IoT deployments.',
        dtc3: 'Collected and pre-processed datasets to support AI model training and improve prediction accuracy.',
        dtc4: 'Designed and built IoT product prototypes for proof-of-concept validation.',
        contrologicRole: 'Engineer - Research and Development',
        contrologicDates: '2020 - Jun 2023',
        contrologic1: 'Designed and developed desktop, web, and mobile applications for internal use and external clients.',
        contrologic2: 'Developed software to read and process sensor and controller data via RS232, RS485, Modbus, and LoRaWAN.',
        contrologic3: 'Connected sensors and hardware tools to existing systems and built POC prototypes to validate new solutions.',
        contrologic4: 'Produced user manuals, system diagrams, man-day estimates, and budget plans.',
        versionLabel: 'Version',
        commitLabel: 'Commit'
    },
    th: {
        pageTitle: 'กรกฎ พงษ์ดี | วิศวกรซอฟต์แวร์',
        headline: 'วิศวกรซอฟต์แวร์ | C++ / .NET | วิศวกรระบบอัตโนมัติ',
        contact: 'ข้อมูลติดต่อ',
        bangkok: 'กรุงเทพมหานคร, ประเทศไทย',
        samutprakarn: 'สมุทรปราการ, ประเทศไทย',
        chonburi: 'ชลบุรี, ประเทศไทย',
        profile: 'ประวัติโดยย่อ',
        profileText: 'นักพัฒนา .NET Full-stack ที่มีพื้นฐานทั้งซอฟต์แวร์และฮาร์ดแวร์ ครอบคลุมเว็บและเดสก์ท็อปแอปพลิเคชัน REST API ระบบสมองกลฝังตัว IoT และการเชื่อมต่อโปรโตคอลอุตสาหกรรม มีประสบการณ์ในธุรกิจประกันภัย ระบบพิมพ์ฉลากอุตสาหกรรม RFID ระบบจำลองสัญญาณรถไฟ และ IoT อุตสาหกรรม',
        education: 'การศึกษา',
        bachelor: 'วิศวกรรมศาสตรบัณฑิต สาขาวิศวกรรมเมคคาทรอนิกส์',
        mut: 'มหาวิทยาลัยเทคโนโลยีมหานคร',
        highVocational: 'ประกาศนียบัตรวิชาชีพชั้นสูง สาขาเทคโนโลยีคอมพิวเตอร์ฮาร์ดแวร์',
        vocational: 'ประกาศนียบัตรวิชาชีพ สาขาอิเล็กทรอนิกส์',
        etech: 'วิทยาลัยเทคโนโลยีภาคตะวันออก (อี.เทค)',
        skills: 'ทักษะ',
        skillFrontend: '<b>Frontend:</b> HTML, CSS3, JavaScript, jQuery, Bootstrap, React',
        skillBackend: '<b>Backend:</b> C# (.NET Framework, .NET Core), C++, Python, Lua, Node.js',
        skillDatabase: '<b>ฐานข้อมูล:</b> Microsoft SQL Server, PostgreSQL, MySQL',
        skillApi: '<b>API และการเชื่อมต่อ:</b> RESTful APIs, AEP, ระบบ RFID',
        skillIot: '<b>Embedded / IoT:</b> Arduino, Raspberry Pi, Node-RED, Linux',
        skillProtocols: '<b>โปรโตคอลอุตสาหกรรม:</b> RS232, RS485, Modbus, LoRaWAN',
        skillEngineering: '<b>วิศวกรรม:</b> SolidWorks, การเขียนแบบวิศวกรรม, อิเล็กทรอนิกส์พื้นฐาน',
        languages: 'ภาษา',
        thaiLanguage: '<b>ภาษาไทย:</b> ภาษาแม่',
        englishLanguage: '<b>ภาษาอังกฤษ:</b> TOEIC 850 (พ.ศ. 2566)',
        workExperience: 'ประสบการณ์ทำงาน',
        tbrokerRole: 'นักพัฒนาซอฟต์แวร์ - ผู้ช่วยผู้จัดการ, นักวิเคราะห์ธุรกิจ',
        tbrokerDates: 'มี.ค. 2568 - พ.ค. 2569',
        tbroker1: 'พัฒนาและดูแลเว็บแอปพลิเคชันเพื่อสนับสนุนงานขายของตัวแทน',
        tbroker2: 'พัฒนาและดูแล REST API ที่เชื่อมต่อกับแพลตฟอร์มภายนอก รวมถึง LINE Chatbot และระบบหลัก',
        tbroker3: 'ดำเนินการทดสอบ SIT และ UAT เพื่อป้องกันข้อผิดพลาดของซอฟต์แวร์ก่อนเผยแพร่',
        tbroker4: 'ประสานงานกับผู้ให้บริการทดสอบการเจาะระบบภายนอกเพื่อค้นหาและแก้ไขช่องโหว่ของเว็บแอปพลิเคชัน',
        tbroker5: 'วางแผนและประเมินเวลาและทรัพยากรสำหรับการพัฒนาตามความต้องการทางธุรกิจ',
        tbroker6: 'ให้การสนับสนุนด้านเทคนิคและแก้ไขปัญหาแก่ตัวแทนและผู้ใช้งาน',
        satoRole: 'นักพัฒนาซอฟต์แวร์ - ฝ่ายบริการลูกค้า',
        satoDates: 'ม.ค. 2567 - ก.พ. 2568',
        sato1: 'พัฒนาเว็บแอปพลิเคชันด้วย .NET เพื่อสนับสนุนระบบพิมพ์ฉลากและโซลูชัน RFID',
        sato2: 'พัฒนาแอปพลิเคชัน AEP สำหรับการพิมพ์แบบ Stand-alone บนเครื่องพิมพ์ SATO',
        sato3: 'พัฒนาโซลูชันซอฟต์แวร์เฉพาะตามความต้องการของลูกค้าแต่ละราย',
        sato4: 'ติดตั้งระบบนอกสถานที่และให้การสนับสนุนแก้ไขปัญหาทั้งหน้างานและระยะไกล',
        sato5: 'จัดทำเอกสารโครงการ เช่น คู่มือผู้ใช้ แผนภาพระบบ การประเมิน Man-day และ Wireframe Demo',
        dtcRole: 'วิศวกรวิจัยและพัฒนา (Hardware IoT)',
        dtcDates: 'ก.ค. 2566 - ก.ย. 2566',
        dtc1: 'ประเมินและทดสอบเซนเซอร์และอุปกรณ์ฮาร์ดแวร์ในการใช้งานจริง',
        dtc2: 'พัฒนาเฟิร์มแวร์ระบบสมองกลฝังตัวและกระบวนการประมวลผลข้อมูลสำหรับระบบ IoT',
        dtc3: 'รวบรวมและเตรียมชุดข้อมูลสำหรับการฝึกโมเดล AI เพื่อช่วยเพิ่มความแม่นยำในการทำนาย',
        dtc4: 'ออกแบบและสร้างต้นแบบผลิตภัณฑ์ IoT เพื่อพิสูจน์แนวคิดและนำเสนอต่อผู้เกี่ยวข้อง',
        contrologicRole: 'วิศวกรวิจัยและพัฒนา',
        contrologicDates: 'พ.ศ. 2563 - มิ.ย. 2566',
        contrologic1: 'ออกแบบและพัฒนาเดสก์ท็อป เว็บ และโมบายแอปพลิเคชันสำหรับใช้งานภายในและลูกค้าภายนอก',
        contrologic2: 'พัฒนาซอฟต์แวร์เพื่ออ่านและประมวลผลข้อมูลจากเซนเซอร์และคอนโทรลเลอร์ผ่าน RS232, RS485, Modbus และ LoRaWAN',
        contrologic3: 'เชื่อมต่อเซนเซอร์และอุปกรณ์ฮาร์ดแวร์เข้ากับระบบเดิม พร้อมสร้างต้นแบบ POC เพื่อทดสอบโซลูชันใหม่',
        contrologic4: 'จัดทำคู่มือผู้ใช้ แผนภาพระบบ การประเมิน Man-day และแผนงบประมาณ',
        versionLabel: 'เวอร์ชัน',
        commitLabel: 'คอมมิต'
    }
};

let currentLanguage = 'en';

function setLanguage(language) {
    const dictionary = translations[language] || translations.en;
    currentLanguage = language;
    document.documentElement.lang = language;
    document.title = dictionary.pageTitle;

    document.querySelectorAll('[data-i18n]').forEach((element) => {
        const value = dictionary[element.dataset.i18n];
        if (value !== undefined) element.textContent = value;
    });

    document.querySelectorAll('[data-i18n-html]').forEach((element) => {
        const value = dictionary[element.dataset.i18nHtml];
        if (value !== undefined) element.innerHTML = value;
    });

    document.querySelectorAll('[data-language]').forEach((button) => {
        const active = button.dataset.language === language;
        button.classList.toggle('active', active);
        button.classList.toggle('btn-primary', active);
        button.classList.toggle('btn-outline-primary', !active);
        button.setAttribute('aria-pressed', active.toString());
    });
}

document.querySelectorAll('[data-language]').forEach((button) => {
    button.addEventListener('click', () => setLanguage(button.dataset.language));
});

setLanguage('en');
