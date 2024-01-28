// Dialog.js
import React from "react";
import styled from "styled-components";

const DialogContainer = styled.div`
  position: fixed;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #2b2b2b;
  padding: 10px 20px;
  border-radius: 5px;
  font-family: "Pixel Font", sans-serif; // Remplacez par la police pixel art de votre choix
  font-size: 16px;
  color: #ffffff;
`;

const Dialog = ({ message }) => {
  return <DialogContainer>{message}</DialogContainer>;
};

export default Dialog;
