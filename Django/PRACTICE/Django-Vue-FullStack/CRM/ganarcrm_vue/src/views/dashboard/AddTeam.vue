<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add team</h1>
            </div>
            <div class="column is-6">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label for="name">Team Name</label>
                        <div class="contorl">
                            <input
                                type="text"
                                class="input"
                                id="name"
                                v-model="name" />
                        </div>
                    </div>
                    <div class="field">
                        <div class="control">
                            <button class="button is-success" type="submit">
                                Submit
                            </button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
    name: "AddTeam",
    data() {
        return {
            name: "",
            // members: [],
            errors: [],
        };
    },
    methods: {
        async submitForm() {
            this.$store.commit("setIsLoading", true);
            const team = {
                name: this.name,
                // members: this.$store.state.user,
            };
            await axios
                .post("/api/v1/teams/", team)
                .then((response) => {
                    console.log(response);
                    toast({
                        message: "Team was created sucessfully",
                        type: "is-success",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: "bottom-right",
                    });
                    this.$store.commit("setTeam", {
                        id: response.data.id,
                        name: this.name,
                    });
                    // this.$router.push("/dashboard");
                    this.$router.push({ name: "Dashboard" });
                })
                .catch((error) => {
                    console.log(error);
                });
            this.$store.commit("setIsLoading", false);
        },
    },
};
</script>
