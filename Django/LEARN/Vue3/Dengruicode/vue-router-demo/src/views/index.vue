<template>
    <div>
        <div>
            首页 - dengruicode.com
            <hr />
        </div>
        <div>
            <!-- <router-link></router-link> 的作用与 <a></a> 类似 -->
            <!-- 但 <router-link></router-link> 支持动态属性绑定 -->
            <router-link to="/content?id=100&title=邓瑞编程">
                查询字符串传参
            </router-link>
            <br />
            <router-link to="/user/007/name/邓瑞">查询路径传参</router-link>
            <br />

            <!-- 动态属性绑定 -->
            <router-link
                :to="{ path: '/content', query: { id: 200, title: 'vue3' } }">
                动态属性绑定-查询字符串传参
            </router-link>
            <br />
            <!-- 路径传参的前提是对应路由具有定义的 name 属性 -->
            <router-link
                :to="{ name: 'member', params: { id: 200, name: 'chaksw' } }">
                动态属性绑定-查询路径传参
            </router-link>
            <br />
            <router-link :to="dynamicStrTo">
                动态属性绑定-查询字符串传参 - 绑定对象
            </router-link>
            <br />
            <router-link :to="dynamicPathTo">
                动态属性绑定-查询路径传参 - 绑定对象
            </router-link>
            <br />

            <button @click="goToStr()">编程式导航 - 1</button>
            <br />
            <button @click="goToPath()">编程式导航 - 2</button>
        </div>
    </div>
</template>

<!-- <script setup> -->
<!-- // 编程式导航
import { useRouter } from "vue-router";
// const dynamicStrTo = {
//     path: "/content",
//     query: { id: 200, title: "vue3" },
// };
// const dynamicPathTo = {
//     name: "member",
//     params: { id: "007", name: "chaksw" },
// };
// 使用 useRouter()
// const router = useRouter();
// 使用 push() 方法 代替 'to' 属性
// const goToStr = () => {
//     // router.push("/content?id=100&title=邓瑞编程");
//	   router.push(dynamicStrTo);
// };
// const goToPath = () => {
//     // router.push({ name: "member", params: { id: 200, name: "chaksw" } });
//     router.push(dynamicPathTo);
// }; -->
<script>
import { useRouter } from "vue-router";
export default {
    data() {
        return {
            router: useRouter(),
            dynamicStrTo: {
                path: "/content",
                query: { id: 200, title: "vue3" },
            },
            dynamicPathTo: {
                name: "member",
                params: { id: "007", name: "chaksw" },
            },
        };
    },
    methods: {
        goToStr() {
            console.log("trigger");
            this.router.push("/content?id=100&title=邓瑞编程");
            this.router.push(this.dynamicStrTo);
        },
        goToPath() {
            console.log(this.dynamicPathTo);
            // router.push({ name: "member", params: { id: 200, name: "chaksw" } });
            this.router.push(this.dynamicPathTo);
        },
    },
};
</script>

<style></style>
