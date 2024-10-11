/*
  This component is used to display a single article, recieved as prop from ArticleList. 
 */

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

const Date = styled.p`
  font-size: 14px;
  color: #888;
`;

const Title = styled.h2`
  margin: 0;
`;

const Description = styled.p`
  margin: 10px 0;
`;

const Author = styled.p`
  font-style: italic;
  color: #888;
`;

const ArticleItem = ({ article }) => (
  <ArticleLink href={article.link} target="_blank" rel="noopener noreferrer">
    <ArticleContainer>
      <ArticleText>
        <Date>{article.date}</Date>
        <Title>{article.title}</Title>
        <Description>{article.description}</Description>
        <Author>{article.author}</Author>
      </ArticleText>
      {article.image && <ArticleImage src={article.image.url} alt={article.title} />}
    </ArticleContainer>
  </ArticleLink>
);

export default ArticleItem;