<!-- List Renderingb v-for -->
<template>
    <h3>List Rendering</h3>
    <p v-for="(item, index) in names">{{ item }} - {{ index }}</p>
    <div v-for="item in results">
        <p>{{ item.title }}</p>
        <img style="width: 250px;" :src="item.avator" :alt="item.id"/>
    </div>
    <div v-for="(value, key, index) in userInfo">
        <p>{{ index }}- {{ key }}-{{ value }}</p>
    </div>
    <p>{{ userInfo.name }}-{{ userInfo.age }}-{{ userInfo.sex }}</p>
</template>

<script>
export default {
    data() {
        return {
            names: ["Chris", "Lyrics", "Murphy"],
            results: [
                {
                    id: 2261677,
                    title: "鄂尔多斯｜感受一座城市的璀璨夜景 感受一座城市，除了白日里的车水马龙，喧嚣繁华之",
                    avator: "https://mma.prnewswire.com/media/1420781/Honeywell_Logo.jpg?p=publish",
                },
                {
                    id: 2261566,
                    title: "成都这家洞穴暗黑风咖啡厅酷毙了！！早C晚A走起☕️ 成都天气这么🔥 咖啡🌟人必备",
                    avator: "https://mma.prnewswire.com/media/1420781/Honeywell_Logo.jpg?p=publish",
                },
                {
                    id: 2261662,
                    title: "[川西新龙-措卡湖]措卡湖吗，意为“乱世从中的黑色海水”，神秘小众 原汁原味。",
                    avator: "https://mma.prnewswire.com/media/1420781/Honeywell_Logo.jpg?p=publish",
                },
            ],
            userInfo: {
                // key : value
                name: "iwen",
                age: 20,
                sex: "male",
            },
        };
    },
};
</script>
