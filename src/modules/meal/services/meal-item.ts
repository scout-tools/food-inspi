import axios from "axios";
const BASE_URL = import.meta.env.VITE_APP_API;
const SERVICE = 'food/meal-item'

export default {

  fetchAll(params: any) {
    return axios.get(`${BASE_URL}/${SERVICE}-read/`, {
      params: params,
    });
  },
  fetchById(id: any) {
    return axios.get(`${BASE_URL}/${SERVICE}-read/${id}/`);
  },
  create(data: any) {
    return axios.post(`${BASE_URL}/${SERVICE}/`, data );
  },
  update(data: any) {
    return axios.put(`${BASE_URL}/${SERVICE}/${data.id}/`, data);
  },
  updatePartical(data: any) {
    return axios.patch(`${BASE_URL}/${SERVICE}/${data.id}/`, data);
  },
  delete(id: any) {
    return axios.delete(`${BASE_URL}/${SERVICE}/${id}`)
  },
  clone(id: any) {
    return axios.post(`${BASE_URL}/${SERVICE}-clone/`, { id })
  },
};
