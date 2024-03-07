import axios from "axios";
const BASE_URL = import.meta.env.VITE_APP_API;

export default {
  fetchCookingPlan(params: any) {
    return axios.get(`${BASE_URL}/food/cooking-plan/`, {
      params: params,
    });
  },
};
