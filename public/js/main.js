import {createApp} from 'vue'

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
            if (this.language == "en") {
                this.language = "de"
            } else if (this.language == "de") {
                this.language = "en"
            }
        }
    },
    mounted() {
        fetch('/elements/' + this.language)
            .then(response => response.json())
            .then(data => this.elements = data);
    },
    updated() {
        fetch('/elements/' + this.language)
            .then(response => response.json())
            .then(data => this.elements = data);
    }
}).mount('#app')