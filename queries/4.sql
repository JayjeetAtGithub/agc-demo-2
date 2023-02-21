SELECT
  mysql.default.HistogramBin(MET.pt, 0, 2000, 100) AS x,
  COUNT(*) AS y
FROM hep
WHERE cardinality(filter(Jet, x -> x.pt > 40)) > 1
GROUP BY mysql.default.HistogramBin(MET.pt, 0, 2000, 100)
ORDER BY x