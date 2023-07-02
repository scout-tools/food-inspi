import { defineStore } from "pinia";

import MealApi from "@/modules/meal/services/meal";
import MealApiDay from "@/modules/meal/services/meal-day";
import MealItemApi from "@/modules/meal/services/meal-item";
import EventApi from "@/modules/meal/services/event";
import ChoiseApi from "@/modules/meal/services/choice";
import ShoppingListApi from "@/modules/meal/services/shopping-list";

import { useCommonStore } from "@/modules/common/store/index";
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
    _mealDay: {},
    _shoppingList: [],
    _physicalActivity: [],
    _isLoading: true,
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
    async fetchPhysicalActivity() {
      try {
        const response = await ChoiseApi.fetchPhysicalActivity();
        this._physicalActivity = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchEvents(params = {}) {
      this._events = [];
      try {
        const response = await EventApi.fetchAll(params);
        this._events = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchEventsSmall(params = {}) {
      try {
        this._isLoading = true;
        const response = await EventApi.fetchSmall(params);
        this._isLoading = false;
        this._events = response.data;
      } catch (error) {
        this._isLoading = false;
        console.log(error);
      }
    },
    async fetchEventById(id: number) {
      this._event = {};
      try {
        const response = await EventApi.fetchById(id);
        this._event = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchMealDayById(id: number) {
      this._mealDay = {};
      try {
        const response = await MealApiDay.fetchById(id);
        this._mealDay = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async createEvent(data: object) {
      try {
        return await EventApi.create(data);
      } catch (error: any) {
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
      } catch (error: any) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async deleteEvent(data: object) {
      try {
        return await EventApi.delete(data);
      } catch (error) {
      }
    },
    async createMeal(data: object) {
      try {
        return await MealApi.create(data);
      } catch (error: any) {
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
      } catch (error: any) {
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
      } catch (error: any) {
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
      } catch (error: any) {
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
      } catch (error: any) {
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
      } catch (error: any) {
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
      } catch (error: any) {
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
    mealDay: (state) => {
      return state._mealDay;
    },
    mealTypes: (state) => {
      return state._mealTypes;
    },
    shoppingList: (state) => {
      return state._shoppingList;
    },
    physicalActivity: (state) => {
      return state._physicalActivity;
    },
    isLoading: (state) => {
      return state._isLoading;
    },
  },
});
