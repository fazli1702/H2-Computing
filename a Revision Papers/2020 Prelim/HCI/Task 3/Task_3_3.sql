SELECT Product.ProductCode, Product.Name, Product.Location, Product.Price, Cake.ServingSize
FROM Product, Cake
WHERE Cake.Shape = 'Circle' 
AND Cake.ProductCode = Product.ProductCode
