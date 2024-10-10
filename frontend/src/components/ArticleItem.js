import React from 'react';
import styled from 'styled-components';

const ArticleLink = styled.a`
  text-decoration: none;
  color: black;
`;

const ArticleContainer = styled.div`
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  border-bottom: 1px solid #ddd;
  margin: 0;
  padding: 20px;
  width: 100%;
  background-color: white;
`;

const ArticleText = styled.div`
  flex: 2;
  padding-right: 20px;
`;

const ArticleImage = styled.img`
  flex: 1;
  max-width: 500px;
  max-height: 200px;
`;

const ArticleItem = ({ article }) => (
  <ArticleLink href={article.link} target="_blank" rel="noopener noreferrer">
    <ArticleContainer>
      <ArticleText>
        <p>{article.published}</p>
        <h2>{article.title}</h2>
        <p>{article.description}</p>
        <p>{article.author}</p>
      </ArticleText>
      {article.image && <ArticleImage src={article.image.url} alt={article.title} />}
    </ArticleContainer>
  </ArticleLink>
);

export default ArticleItem;