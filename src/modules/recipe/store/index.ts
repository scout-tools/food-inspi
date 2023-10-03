import { defineStore } from "pinia";

import RecipeApi from "@//modules/recipe/services/recipe.ts";
import RecipeItemApi from "@//modules/recipe/services/recipe-item.ts";

import { useCommonStore } from "@/modules/common/store/index.ts";
const commonStore = useCommonStore();

export const useRecipeStore = defineStore("recipe", {
  state: () => ({
    _recipes: [],
    _recipesVerified: [],
    _recipesPublic: [],
    _recipeDetail: {},
    _recipeItem: {},
    _myRecipies: [],
    _isLoading: true,
    _createRecipeData: [{
      stepId: 1,
      name: '',
      description: '',
      mealType: ''
    }, {
      stepId: 2,
      recipeItems: [],
    }, {
      stepId: 3,
    }]
  }),

  actions: {
    addCreateRecipeData(step: number, data: object) {
      this._createRecipeData[step-1] = data;
    },
    async fetchRecipes(params = {}) {
      try {
        this._isLoading = true;
        const response = await RecipeApi.fetchAll(params);
        this._isLoading = false;
        this._recipes = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchVerified(params = {}) {
      try {
        this._isLoading = true;
        const response = await RecipeApi.fetchVerified(params);
        this._isLoading = false;
        this._recipesVerified = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchPublicRecipies(params = {}) {
      this._isLoading = true;
      try {
        const response = await RecipeApi.fetchPublicRecipies(params);
        this._isLoading = false;
        this._recipesPublic = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchMyRecipies(params = {}) {
      try {
        this._isLoading = true;
        const response = await RecipeApi.fetchMyRecipies(params);
        this._isLoading = false;
        this._myRecipies = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async fetchRecipeById(id: number) {
      try {
        const response = await RecipeApi.fetchById(id);
        this._recipeDetail = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async createRecipe(data: object) {
      try {
        return await RecipeApi.create(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError("Schwerer Server Fehler");
        }
      }
    },
    async updateRecipe(data: object) {
      try {
        return await RecipeApi.update(data?.id, data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError("Schwerer Server Fehler");
        }
      }
    },
    async multiplyRecipeItems(data: object) {
      try {
        return await RecipeApi.multiplyRecipeItems(data);
      } catch (error) {}
    },
    async deleteRecipe(data: object) {
      try {
        return await RecipeApi.delete(data);
      } catch (error) {}
    },
    //
    async fetchRecipeItemById(id: number) {
      try {
        const response = await RecipeItemApi.fetchById(id);
        this._recipeItem = response.data;
      } catch (error) {
        alert(error);
        console.log(error);
      }
    },
    async createRecipeItem(data: object) {
      try {
        return await RecipeItemApi.create(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError("Schwerer Server Fehler");
        }
      }
    },
    async updateRecipeItem(data: object) {
      try {
        return await RecipeItemApi.update(data);
      } catch (error) {
        if (error.response.status === 400) {
          commonStore.showError(error.response.data);
        } else if (error.response.status === 500) {
          commonStore.showError("Schwerer Server Fehler");
        }
      }
    },
    async deleteRecipeItem(id: Number) {
      try {
        return await RecipeItemApi.delete(id);
      } catch (error) {}
    },
    async cloneRecipe(id: Number) {
      try {
        return await RecipeApi.clone(id);
      } catch (error) {}
    },
  },
  getters: {
    recipes: (state) => {
      return state._recipes;
    },
    recipesVerified: (state) => {
      return state._recipesVerified;
    },
    recipesPublic: (state) => {
      return state._recipesPublic;
    },
    myRecipies: (state) => {
      return state._myRecipies;
    },
    recipeDetail: (state) => {
      return state._recipeDetail;
    },
    recipeItem: (state) => {
      return state._recipeItem;
    },
    createRecipeData: (state) => {
      return state._createRecipeData;
    },
    isLoading: (state) => {
      return state._isLoading;
    }
  },
});
