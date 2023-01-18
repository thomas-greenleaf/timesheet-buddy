import { InjectionKey } from "vue";
import { createStore, useStore as baseUseStore, Store } from "vuex";

export interface State {
  user: {
    userId: null | number;
    userName: null | string;
  };
  fastApiEnd: string;
}

// define injection key
export const key: InjectionKey<Store<State>> = Symbol();

export const store = createStore<State>({
  state: {
    user: {
      userId: null,
      userName: null,
    },
    fastApiEnd: "http://localhost:8081/",
  },
  mutations: {
    fictitiousLogin(state) {
      state.user.userId = 1;
      state.user.userName = "tgreenleaf";
    },
    logout(state) {
      state.user.userId = null;
      state.user.userName = null;
    },
  },
});

export function useStore() {
  return baseUseStore(key);
}
