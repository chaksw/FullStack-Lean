<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Clients</h1>
                <template></template>
                <router-link
                    :to="{ name: 'AddClient' }"
                    v-if="$store.state.team.max_clients > num_clients"
                    class="button is-primary">
                    Add client
                </router-link>
                <div class="notification is-danger" v-else>
                    You have reached the top of your limitation. Please upgrade!
                </div>
                <hr />
                <form action="" @submit.prevent="getClients">
                    <div class="field has-addons">
                        <div class="control">
                            <input type="text" class="input" v-model="query" />
                        </div>
                        <div class="control">
                            <button class="button is-success">Search</button>
                        </div>
                    </div>
                </form>
            </div>
            <div class="column is-12">
                <template v-if="clients.length">
                    <table class="table is-fullwidth">
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Contact Person</th>
                                <th>Details</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="client in clients"
                                v-bind:key="client.id">
                                <td>{{ client.name }}</td>
                                <td>{{ client.contact_person }}</td>
                                <td>
                                    <router-link
                                        :to="{
                                            name: 'Client',
                                            params: { id: client.id },
                                        }">
                                        Detail
                                    </router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <div class="buttons">
                        <button
                            class="button is-light"
                            @click="goToPreviousPage()"
                            v-if="showPreviousButton">
                            Previous
                        </button>
                        <button
                            class="button is-light"
                            @click="goToNextPage()"
                            v-if="showNextButton">
                            Next
                        </button>
                    </div>
                </template>
                <template v-else>
                    <p>You don't have any clients yets...</p>
                </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "Clients",
    data() {
        return {
            clients: [],
            showNextButton: false,
            showPreviousButton: false,
            currentPage: 1,
            query: "",
            num_clients: 0,
        };
    },
    mounted() {
        this.getClients();
    },
    methods: {
        goToNextPage() {
            this.currentPage += 1;
            this.getClients();
        },
        goToPreviousPage() {
            this.currentPage -= 1;
            this.getClients();
        },
        async getClients() {
            this.$store.commit("setIsLoading", true);

            await axios.get("/api/v1/clients/").then((response) => {
                this.num_clients = response.data.count;
            });
            await axios
                .get(
                    `/api/v1/clients/?page=${this.currentPage}&search=${this.query}`
                )
                .then((response) => {
                    this.clients = response.data.results;
                    // console.log(response.data.next);
                    this.showNextButton = response.data.next ? true : false;
                    this.showPreviousButton = response.data.previous
                        ? true
                        : false;
                })
                .catch((error) => {
                    console.log(error);
                });

            this.$store.commit("setIsLoading", false);
        },
    },
};
</script>
