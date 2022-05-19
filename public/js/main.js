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
    methods: {},
    mounted() {
        fetch('/elements/' + this.language)
            .then(response => response.json())
            .then(data => this.elements = data);
    }
}).mount('#app')