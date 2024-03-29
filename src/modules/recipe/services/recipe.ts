import axios from "axios";
const BASE_URL = import.meta.env.VITE_APP_API;
const SERVICE = 'food/recipe'

export default {

  fetchAll(params: any) {
    return axios.get(`${BASE_URL}/food/recipe-read/`, {
      params: params,
    });
  },
  fetchVerified(params: any) {
    return axios.get(`${BASE_URL}/food/recipe-read-verified/`, {
      params: params,
    });
  },
  fetchPublicRecipies(params: any) {
    return axios.get(`${BASE_URL}/food/recipe-read-user/`, {
      params: params,
    });
  },
  fetchMyRecipies(params: any) {
    return axios.get(`${BASE_URL}/food/my-recipe-read/`, {
      params: params,
    });
  },
  fetchById(id: any) {
    return axios.get(`${BASE_URL}/${SERVICE}/${id}/`);
  },

  create(data: any) {
    return axios.post(`${BASE_URL}/${SERVICE}/`, data );
  },
  update(id: any, data: any) {
    return axios.put(`${BASE_URL}/${SERVICE}/${id}/`, data);
  },
  multiplyRecipeItems(data: any) {
    return axios.post(`${BASE_URL}/food/multiply-recipe-items/`, data);
  },
  delete(id: any) {
    return axios.delete(`${BASE_URL}/${SERVICE}/${id}`)
  },
  clone(id: any) {
    return axios.post(`${BASE_URL}/${SERVICE}-clone/`, { id })
  },
};
