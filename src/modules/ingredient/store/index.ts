import { defineStore } from "pinia";

import IngredientApi from "@/modules/ingredient/services/ingredient";
import PortionsApi from "@/modules/ingredient/services/portion";
import PackageApi from "@/modules/ingredient/services/package";
import PriceApi from "@/modules/ingredient/services/price";
import RetailerApi from "@/modules/ingredient/services/retailer";
import MeasuringUnitApi from "@/modules/ingredient/services/measuringUnit";

import { useCommonStore } from "@/modules/common/store/index.ts";
import measuringUnit from "../services/measuringUnit";
const commonStore = useCommonStore();

export const useIngredientStore = defineStore("ingredient", {
  state: () => ({
    _ingredients: [],
    _ingredientDetail: {},
    _portions: [],
    _prices: [],
    _packages: [],
    _retailers: [],
    _measuringUnits: [],
  }),

  actions: {
    async fetchIngredients(params = {}) {
      try {
        const response = await IngredientApi.fetchAll(params);
        this._ingredients = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchIngredientById(id: number) {
      try {
        const response = await IngredientApi.fetchById(id);
        this._ingredientDetail = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async createIngredient(data: object) {
      try {
        return await IngredientApi.create(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async updateIngredient(data: object) {
      try {
        return await IngredientApi.update(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async deleteIngredient(data: object) {
      try {
        return await IngredientApi.delete(data);
      } catch (error) {
      }
    },
    async fetchPortions(params = {}) {
      try {
        const response = await PortionsApi.fetchAll(params);
        this._portions = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async createPortion(data: object) {
      try {
        return await PortionsApi.create(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async fetchPackages(params = {}) {
      try {
        const response = await PackageApi.fetchAll(params);
        this._packages = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchPrices(params = {}) {
      try {
        const response = await PriceApi.fetchAll(params);
        this._prices = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async createPrice(data: object) {
      try {
        return await PriceApi.create(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async deletePrice(data: object) {
      try {
        return await PriceApi.delete(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError('Schwerer Server Fehler');
        }
      }
    },
    async fetchRetailers(params = {}) {
      try {
        const response = await RetailerApi.fetchAll(params);
        this._retailers = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchMeasuringUnit(params = {}) {
      try {
        const response = await MeasuringUnitApi.fetchAll(params);
        this._measuringUnits = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
  },
  getters: {
    ingredients: (state) => {
      return state._ingredients;
    },
    ingredientDetail: (state) => {
      return state._ingredientDetail;
    },
    portions: (state) => {
      return state._portions;
    },
    packages: (state) => {
      return state._packages;
    },
    prices: (state) => {
      return state._prices;
    },
    retailers: (state) => {
      return state._retailers;
    },
    measuringUnits: (state) => {
      return state._measuringUnits;
    },
  },
});
