import React from 'react';
import { useTranslation } from 'react-i18next';
import styled from 'styled-components';
import Header from './components/Header';  // Adjust path as needed
import ArticleList from './components/ArticleList';  // Adjust path as needed

// Container for the whole app
const AppContainer = styled.div`
  font-family: Arial, sans-serif;
  margin: 0 auto;
  padding: 20px;
  background-color: #f1f1f1;
`;

const App = () => {
  const { i18n } = useTranslation();  // Access the i18n instance to use the language state

  return (
    <AppContainer>
      <ArticleList />

      <p style={{ textAlign: 'center', marginTop: '20px' }}>
        Current Language: {i18n.language.toUpperCase()}
      </p>
    </AppContainer>
  );
};

export default App;