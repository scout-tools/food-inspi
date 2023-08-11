import axios from "axios";
const BASE_URL = import.meta.env.VITE_APP_API;

export default {
  fetchMealTypes() {
    return axios.get(`${BASE_URL}/food/meal-types`);
  },
  fetchRecipeStatuses() {
    return axios.get(`${BASE_URL}/food/recipe-statuses`);
  },
  fetchPhysicalActivity() {
    return axios.get(`${BASE_URL}/food/physical-activity`);
  },
};
