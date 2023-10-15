import axios from "axios";
const BASE_URL = import.meta.env.VITE_APP_API;
const SERVICE = 'food/meal-event'

export default {

  fetchAll(params: any) {
    return axios.get(`${BASE_URL}/${SERVICE}-read/`, {
      params: params,
    });
  },
  fetchSmall(params: any) {
    return axios.get(`${BASE_URL}/${SERVICE}-read-small/`, {
      params: params,
    });
  },
  fetchMyEvents(params: any) {
    return axios.get(`${BASE_URL}/food/my-event-read/`, {
      params: params,
    });
  },
  fetchMyEventsSmall(params: any) {
    return axios.get(`${BASE_URL}/food/my-event-small-read/`, {
      params: params,
    });
  },
  fetchPublicEvents(params: any) {
    return axios.get(`${BASE_URL}/food/public-event-read/`, {
      params: params,
    });
  },
  fetchPublicEventsSmall(params: any) {
    return axios.get(`${BASE_URL}/food/public-event-small-read/`, {
      params: params,
    });
  },
  fetchApprovedEvents(params: any) {
    return axios.get(`${BASE_URL}/food/approved-event-read/`, {
      params: params,
    });
  },
  fetchApprovedEventsSmall(params: any) {
    return axios.get(`${BASE_URL}/food/approved-event-small-read/`, {
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
  delete(data: any) {
    return axios.delete(`${BASE_URL}/${SERVICE}/${data.id}`)
  },
  clone(id: any) {
    return axios.post(`${BASE_URL}/${SERVICE}-clone/`, { id })
  },
};
