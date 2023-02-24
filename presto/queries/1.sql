SELECT
  mysql.default.HistogramBin(MET.pt, 0, 2000, 100) AS x,
  COUNT(*) AS y
FROM hep
GROUP BY mysql.default.HistogramBin(MET.pt, 0, 2000, 100)
ORDER BY x