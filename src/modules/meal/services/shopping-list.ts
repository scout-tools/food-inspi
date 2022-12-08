import axios from "axios";
const BASE_URL = import.meta.env.VITE_APP_API;
const SERVICE = 'food/shopping-list'

export default {

  fetchAll(params: any) {
    return axios.get(`${BASE_URL}/${SERVICE}/`, {
      params: params,
    });
  },
};
