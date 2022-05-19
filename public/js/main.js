import {createApp} from 'vue'

let id = 0

createApp({
    data() {
        return {
            message: 'world',
            language: 'en'
        }
    },
    methods: {
    }
}).mount('#app')