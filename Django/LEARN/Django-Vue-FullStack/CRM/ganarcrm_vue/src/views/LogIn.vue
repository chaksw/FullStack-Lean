<template>
    <div class="container">
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <h1 class="title">Log In</h1>
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label for="email">Email</label>
                        <div class="control">
                            <input
                                type="email"
                                class="input"
                                name="email"
                                id="email"
                                v-model="username" />
                        </div>
                    </div>
                    <div class="field">
                        <label for="password1">Password</label>
                        <div class="control">
                            <input
                                type="password"
                                class="input"
                                name="password1"
                                id="password1"
                                v-model="password" />
                        </div>
                    </div>
                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="errors">
                            {{ error }}
                        </p>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "LogIn",
    data() {
        // with return an object with initial data defined below
        return {
            username: "",
            password: "",
            errors: [],
        };
    },
    methods: {
        async submitForm() {
            this.$store.commit("setIsLoading", true);

            axios.defaults.headers.common["Authorization"] = "";
            localStorage.removeItem("token");
            const formData = {
                username: this.username,
                password: this.password,
            };
            await axios
                .post("api/v1/token/login/", formData)
                .then((response) => {
                    const token = response.data.auth_token;
                    console.log(token);
                    // commit is used to call mutation function in LogIn
                    this.$store.commit("setToken", token);
                    axios.defaults.headers.common["Authorization"] =
                        "Token " + token;
                    localStorage.setItem("token", token);
                })
                .catch((error) => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(
                                `${property}:${error.response.data[property]}`
                            );
                        }
                    } else if (error.message) {
                        this.errors.push(
                            "Something went wrong. Please try again!"
                        );
                    }
                });
            await axios
                .get("api/v1/users/me")
                .then((response) => {
                    this.$store.commit("setUser", {
                        id: response.data.id,
                        username: response.data.username,
                    });
                    localStorage.setItem("username", response.data.username);
                    localStorage.setItem("userid", response.data.id);
                })
                .catch((error) => {
                    console.log(error);
                });

            await axios
                .get("api/v1/teams/get_my_team/")
                .then((response) => {
                    console.log(response.data);
                    this.$store.commit("setTeam", {
                        id: response.data.id,
                        name: response.data.name,
                        plan: response.data.plan.name,
                        max_leads: response.data.plan.max_leads,
                        max_clients: response.data.plan.max_clients,
                    });
                    // localStorage.setItem("team_name", response.data.username);
                    // localStorage.setItem("team_id", response.data.id);
                    // this.$router.push("dashboard/my-account");
                    this.$router.push({ name: "MyAccount" });
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
    },
};
</script>
