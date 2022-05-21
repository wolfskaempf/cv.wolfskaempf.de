import {createApp} from '../dist/vue.esm-browser.js'

createApp({
    data() {
        return {
            loading: true,
            error: null,
            elements: {},
            language: 'en'
        }
    },
    methods: {
        switchLanguage() {
            if (this.language === "en") {
                this.language = "de"
            } else if (this.language === "de") {
                this.language = "en"
            }
            fetch('/elements/' + this.language)
                .then(response => response.json())
                .then(data => this.elements = data);
        }
    },
    mounted() {
        fetch('/elements/' + this.language)
            .then(response => response.json())
            .then(data => this.elements = data);
    },
}).mount('#app')