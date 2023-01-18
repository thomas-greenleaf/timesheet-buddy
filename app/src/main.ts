import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "./index.css";
import { createAuth0 } from "@auth0/auth0-vue";
import { store, key } from "./store";

const app = createApp(App);

app.use(router);

app.use(
  createAuth0({
    domain: "dev-mljfqult.us.auth0.com",
    client_id: "yjjxau7AmDPVbtnsvx3P5yq9HCDLbKQv",
    redirect_uri: window.location.origin,
  })
);

app.use(store, key);
store.commit("fictitiousLogin");

app.mount("#app");
