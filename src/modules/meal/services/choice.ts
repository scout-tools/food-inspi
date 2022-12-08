import axios from "axios";
const BASE_URL = import.meta.env.VITE_APP_API;

export default {
  fetchMealTypes() {
    return axios.get(`${BASE_URL}/food/meal-types`);
  },
};
