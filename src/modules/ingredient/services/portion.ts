import axios from "axios";
const BASE_URL = import.meta.env.VITE_APP_API;
const SERVICE = 'food/portion'

export default {

  fetchAll(params: any) {
    return axios.get(`${BASE_URL}/${SERVICE}-read/`, {
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
    return axios.put(`${BASE_URL}/${SERVICE}/${id}`, data);
  },

  delete(data: any) {
    return axios.delete(`${BASE_URL}/${SERVICE}/${data.id}`)
  },
};
