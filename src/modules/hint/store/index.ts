import { defineStore } from "pinia";

import HintApi from "@/modules/hint/services/hint";


export const useHintStore = defineStore("hint", {
  state: () => ({
    _hints: [],
    _hint: [],
  }),

  actions: {
    async fetchHints(params = {}) {
      try {
        const response = await HintApi.fetchAll(params);
        this._hints = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchHintById(id: Number) {
      try {
        const response = await HintApi.fetchById(id);
        this._hint = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
  getters: {
    hints: (state) => {
      return state._hints;
    },
    hint: (state) => {
      return state._hint;
    },
  },
});
