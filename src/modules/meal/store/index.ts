import { defineStore } from "pinia";

import MealApi from "@/modules/meal/services/meal";
import MealItemApi from "@/modules/meal/services/meal-item";
import EventApi from "@/modules/meal/services/event";
import ChoiseApi from "@/modules/meal/services/choice";
import ShoppingListApi from "@/modules/meal/services/shopping-list";

import { useCommonStore } from "@/modules/common/store/index.ts";
const commonStore = useCommonStore();

export const useMealStore = defineStore("meal", {
  state: () => ({
    _event: {},
    _events: [{
      stepId: 1,
      name: '',
      description: '',
      mealType: ''
    }],
    _mealTypes: [],
    _shoppingList: []
  }),

  actions: {
    async fetchMealTypes() {
      try {
        const response = await ChoiseApi.fetchMealTypes();
        this._mealTypes = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchEvents(params = {}) {
      try {
        const response = await EventApi.fetchAll(params);
        this._events = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchEventById(id: number) {
      try {
        const response = await EventApi.fetchById(id);
        this._event = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async createEvent(data: object) {
      try {
        return await EventApi.create(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async updateEvent(data: object) {
      try {
        return await EventApi.update(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async deleteEvent(data: object) {
      try {
        debugger;
        return await EventApi.delete(data);
      } catch (error) {
      }
    },
    async createMeal(data: object) {
      try {
        return await MealApi.create(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async updateMeal(data: object) {
      try {
        return await MealApi.update(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async deleteMeal(id: number) {
      try {
        return await MealApi.delete(id);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async createMealItem(data: object) {
      try {
        return await MealItemApi.create(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async updateMealItem(data: object) {
      try {
        return await MealItemApi.update(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async deleteMealItem(data: object) {
      try {
        return await MealItemApi.delete(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async fetchShoppingList(params = {}) {
      try {
        const response = await ShoppingListApi.fetchAll(params);
        this._shoppingList = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
  getters: {
    events: (state) => {
      return state._events;
    },
    event: (state) => {
      return state._event;
    },
    mealTypes: (state) => {
      return state._mealTypes;
    },
    shoppingList: (state) => {
      return state._shoppingList;
    },

  },
});
