import Keycloak, { KeycloakError, KeycloakInitOptions, KeycloakProfile } from "keycloak-js";
import { useAuthStore } from "@/modules/auth/store";

const config = {
  url: import.meta.env.VITE_APP_KEYCLOAK_URL,
  realm: import.meta.env.VITE_APP_KEYCLOAK_REALM,
  clientId: import.meta.env.VITE_APP_KEYCLOAK_CLIENT_ID,
};

const initOptions: KeycloakInitOptions = {
  checkLoginIframe: false, // default
  onLoad: "check-sso",
  silentCheckSsoFallback: false,
};

export const keycloak = new Keycloak(config);

function setStoreValues() {
  const authStore = useAuthStore();
  authStore._isAuth = keycloak.authenticated;
  authStore._accessToken = keycloak.token;
  authStore._isKeycloakInit = true;

  if (keycloak.authenticated) {
    keycloak
      .loadUserInfo()
      .then((test) => {
        authStore._user = keycloak.userInfo;
      })
      .catch((error) => {
        console.log(`error while loading userinfo: ${error}`);
      });
  } else {
    authStore._user = {};
  }
}

function onReady(authenticated: boolean) {
  console.log('onReady')
  setStoreValues();
}

function onAuthError(error: KeycloakError) {
  console.log('onAuthError')
  setStoreValues();
}

function onAuthLogout() {
  console.log('onAuthLogout')
  setStoreValues();
}

function onTokenExpired() {
  console.log('onTokenExpired')
  keycloak
    .updateToken(30)
    .then(() => {
      setStoreValues();
    })
    .catch((error) => {
      setStoreValues();
    });
}

function onActionUpdate(status: "success" | "cancelled" | "error") {
  console.log('onActionUpdate')
  setStoreValues();
}

function onAuthRefreshError() {
  console.log('onAuthRefreshError')
  setStoreValues();
}

function onAuthRefreshSuccess() {
  console.log('onAuthRefreshSuccess')
  setStoreValues();
}

function onAuthSuccess() {
  console.log('onAuthSuccess')
  if (!keycloak.authenticated) {
    location.reload()
  }
}

export default function () {
  keycloak.onReady = onReady;
  keycloak.onAuthError = onAuthError;
  keycloak.onAuthLogout = onAuthLogout;
  keycloak.onTokenExpired = onTokenExpired;
  keycloak.onActionUpdate = onActionUpdate;
  keycloak.onAuthRefreshError = onAuthRefreshError;
  keycloak.onAuthRefreshSuccess = onAuthRefreshSuccess;
  keycloak.onAuthSuccess = onAuthSuccess;
  keycloak.init(initOptions);
}
