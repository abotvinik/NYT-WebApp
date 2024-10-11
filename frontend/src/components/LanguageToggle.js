import React from 'react';
import styled from 'styled-components';
import { useTranslation } from 'react-i18next';

const LanguageContainer = styled.div`
  cursor: pointer;
  font-size: 14px;
`;

const LanguageToggle = () => {
  const { i18n } = useTranslation();

  const switchLanguage = () => {
    const newLang = i18n.language === 'en' ? 'es' : 'en';
    i18n.changeLanguage(newLang);
  };

  return (
    <LanguageContainer onClick={switchLanguage}>
      Toggle Language
    </LanguageContainer>
  );
};

export default LanguageToggle;