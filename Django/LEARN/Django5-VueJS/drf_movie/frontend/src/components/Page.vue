<template>
    <div
        id="footer"
        class="flex items-center justify-center text-gray-500 pb-4">
        <!-- 上一页 -->
        <span v-if="info.previous" @click="goToPage(prePage)" class="page-link">
            <button class="w-8 h-8 rounded mx-1 my-1 bg-gray-300">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 mx-auto"
                    viewBox="0 0 20 20"
                    fill="currentColor">
                    <path
                        fill-rule="evenodd"
                        d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                        clip-rule="evenodd" />
                </svg>
            </button>
        </span>
        <a v-for="page in pages" :key="page" class="page-link">
            <button
                v-if="page === '...'"
                class="w-8 h-8 rounded mx-1 my-1 bg-gray-300">
                {{ page }}
            </button>
            <button
                v-else-if="page === this.current"
                class="w-8 h-8 rounded mx-1 my-1 bg-blue-500 text-white">
                {{ page }}
            </button>
            <button
                v-else
                @click="goToPage(page)"
                class="w-8 h-8 rounded mx-1 my-1 bg-gray-300">
                {{ page }}
            </button>
        </a>
        <!-- 遍历每一页 -->
        <!-- <div class="page-link">
            <button
                class="w-8 h-8 rounded mx-1 my-1 bg-blue-500 text-white"></button>
            <button class="w-8 h-8 rounded mx-1 my-1"></button>
            <button class="w-8 h-8 rounded mx-1 my-1 bg-gray-300"></button>
        </div> -->
        <!-- 下一页 -->
        <a v-if="info.next" @click="goToPage(nextPage)" class="page-link">
            <button class="w-8 h-8 rounded mx-1 my-1 bg-gray-300">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5 mx-auto"
                    viewBox="0 0 20 20"
                    fill="currentColor">
                    <path
                        fill-rule="evenodd"
                        d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                        clip-rule="evenodd" />
                </svg>
            </button>
        </a>
    </div>
</template>

<script>
export default {
    name: "Page",
    data: () => {
        return {
            current: 1,
        };
    },
    mounted() {
        this.current = this.getPageFromUrl();
    },
    props: {
        info: Array,
    },
    computed: {
        lastPage() {
            let pageSize = 12;
            return Math.ceil(this.info.count / pageSize);
        },
        // 获取上一页
        prePage() {
            if (this.current > 1) {
                return this.current - 1;
            }
            return 1;
        },
        // 获取下一页
        nextPage() {
            if (this.current < this.lastPage) {
                return this.current + 1;
            }
            return this.current;
        },
        // 基于当前页显示可跳转的页面
        pages() {
            const pages = [];
            for (let i = 1; i <= this.lastPage; i++) {
                if (
                    i === 1 ||
                    i === this.lastPage ||
                    (i <= this.current + 1 && i >= this.current - 1)
                ) {
                    pages.push(i);
                } else if (pages[pages.length - 1] !== "...") {
                    pages.push("...");
                }
            }
            return pages;
        },
    },

    methods: {
        getPageFromUrl() {
            const page = Number(this.$route.query.page);
            return page ? page : 1;
        },
        goToPage(page) {
            // this.$router.push：这是 Vue Router 中的导航方法，用于编程式导航到指定的路由。
            // { query: { page } }：这是传递的查询对象，将 page 参数设置为当前的 page 变量值。这样会自动生成类似 ?page=2 的查询字符串附加到 URL 中。
            // 假设当前 url 为 /movie
            // 执行 this.$router.push({ query: { page: 2 } }); 新的 url 会变成 movie/?page=2
            // alert(page);
            this.$router.push({ query: { page } });
            this.current = page;
        },
    },
};
</script>
