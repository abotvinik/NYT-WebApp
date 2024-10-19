/*
  Processes the API response and displays the list of articles.
  Also sends article metadata to the Header component.
 */

import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ArticleItem from './ArticleItem';
import styled from 'styled-components';
import { useTranslation } from 'react-i18next';
import Header from './Header';

const ListContainer = styled.div`
  max-width: 800px;
  margin: 40px auto;
`;

const ArticleList = () => {
  const [articles, setArticles] = useState([]);
  const [logo, setLogo] = useState(null);
  const [loading, setLoading] = useState(true);
  const { i18n } = useTranslation();

  useEffect(() => {
    const fetchArticles = async () => {
      setLoading(true);
      try {
        const source = axios.CancelToken.source();
        const timeoutId = setTimeout(() => {
          source.cancel("Timeout");
          setLoading(false);
        }, 60000);

        const backendUrl = `${window.location.href}/rss`;
        console.log('Backend URL: ', backendUrl);
        const response = await axios.get(`${backendUrl}/${i18n.language}`);
        clearTimeout(timeoutId);
        setArticles(response.data.articles);
        setLogo(response.data.logo);
      } catch (error) {
        console.error('Error fetching articles: ', error);
      } finally {
        setLoading(false);
      }
    };
    fetchArticles();
  }, [i18n.language]);

  return (
    <div>
      <Header logo={logo}/>
      <ListContainer>
        {loading ? (
          <p>Loading articles...</p>
        ) : (
          articles.map((article, index) => (
            <ArticleItem key={index} article={article} />
          ))
        )}
      </ListContainer>
    </div>
  );
};

export default ArticleList;