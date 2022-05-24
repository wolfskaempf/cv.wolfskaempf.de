import {createApp} from '../dist/vue.esm-browser.js'

createApp({
    data() {
        return {
            show_js_warning: false,
            elements: {},
            experiences: null,
            education: null,
            volunteering: null,
            trivia: null,
            personal_data: {},
            personal_data_success: false,
            language: 'de'
        }
    },
    methods: {
        fetchData() {
            fetch('/elements/' + this.language)
                .then(response => response.json())
                .then(data => this.elements = data);
            fetch('/experiences/' + this.language)
                .then(response => response.json())
                .then(data => this.experiences = data);
            fetch('/education/' + this.language)
                .then(response => response.json())
                .then(data => this.education = data);
            fetch('/volunteering/' + this.language)
                .then(response => response.json())
                .then(data => this.volunteering = data);
            fetch('/trivia/' + this.language)
                .then(response => response.json())
                .then(data => this.trivia = data);
        },
        switchLanguage() {
            if (this.language === "en") {
                this.language = "de"
            } else if (this.language === "de") {
                this.language = "en"
            }
            this.fetchData();
        },
        processPersonalDataPromise(data) {
            if (data['status_code'] !== 401) {
                this.personal_data = data;
                this.personal_data_success = true;
            }
        }
    },
    mounted() {
        this.fetchData();
        fetch('/personal_data?secret=' + document.location.hash.substring(1))
            .then(response => response.json())
            .then(data => this.processPersonalDataPromise(data));
    },
}).mount('#app')