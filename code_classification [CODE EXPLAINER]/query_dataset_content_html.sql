SELECT DISTINCT
  content
FROM
  `bigquery-public-data.github_repos.contents` as contents
JOIN
  `bigquery-public-data.github_repos.files` as files
ON
  contents.id = files.id
WHERE
  files.path LIKE '%.htm' AND
  content IS NOT NULL
LIMIT
  2500;
