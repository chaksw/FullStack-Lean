import { fileURLToPath, URL } from "node:url";
import path from "path";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    resolve: {
        alias: {
            // 配置路径别名, 当输入@符号是，会自动找到项目下的src目录
            // 方法1: "@": path.resolve(__dirname, "src"),
            // 方法2:
            "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
    },
});
