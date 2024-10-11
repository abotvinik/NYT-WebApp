import React from 'react';
import styled from 'styled-components';
import LanguageToggle from './LanguageToggle';

const HeaderContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  position: sticky;
  top: 0;
  background-color: white;
  border-bottom: 1px solid black;
  z-index: 100;
  background-color: #f1f1f1;
`;

const Logo = styled.img`
  height: 40px;
`;

const Date = styled.div`
  font-size: 14px;
  color: #888;
`;

const Header = ({ logo }) => {
  const today = new window.Date().toDateString();
  return (
    <HeaderContainer>
      <Date>{today}</Date>
      {logo && <Logo src={logo} alt="Logo" />} 
      <LanguageToggle />
    </HeaderContainer>
  );
};

export default Header;