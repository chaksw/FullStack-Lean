import './assets/main.css';
import { createApp } from 'vue';
import App from './App.vue';
import channelServ from './services/channel';
async function test() {
    var channels = await channelServ.getChannels();
    console.log(channels);
}

test();
createApp(App).mount('#app');
