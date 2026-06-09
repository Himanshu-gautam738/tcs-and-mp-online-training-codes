CREATE TABLE Vendor_Dim (
    VendorKey INT PRIMARY KEY,
    VendorName VARCHAR(100)
);

INSERT INTO Vendor_Dim VALUES
(0,'UNKNOWN'),
(-1,'NULL');

CREATE TABLE Feed_Dim (
    FeedKey INT PRIMARY KEY,
    FeedName VARCHAR(100)
);

INSERT INTO Feed_Dim VALUES
(0,'UNKNOWN'),
(-1,'NULL');

CREATE TABLE SourceFeed_Dim (
    SourceFeedKey INT PRIMARY KEY,
    SourceFeedName VARCHAR(100)
);

INSERT INTO SourceFeed_Dim VALUES
(0,'UNKNOWN'),
(-1,'NULL');

CREATE TABLE Date_Dim (
    DateKey INT PRIMARY KEY,
    FullDate DATE
);

INSERT INTO Date_Dim VALUES
(0,NULL),
(-1,NULL);

CREATE TABLE Exchange_Dim (
    ExchangeKey INT PRIMARY KEY,
    ExchangeName VARCHAR(100)
);

INSERT INTO Exchange_Dim VALUES
(0,'UNKNOWN'),
(-1,'NULL');

CREATE TABLE PriceType_Dim (
    PriceTypeKey INT PRIMARY KEY,
    PriceTypeName VARCHAR(100)
);

INSERT INTO PriceType_Dim VALUES
(0,'UNKNOWN'),
(-1,'NULL');

CREATE TABLE Security_Dim (
    SecurityKey INT PRIMARY KEY,
    SecurityName VARCHAR(100)
);

INSERT INTO Security_Dim VALUES
(0,'UNKNOWN'),
(-1,'NULL');

CREATE TABLE Issue_Dim (
    IssueKey INT PRIMARY KEY,
    IssueName VARCHAR(100)
);

INSERT INTO Issue_Dim VALUES
(0,'UNKNOWN'),
(-1,'NULL');

CREATE TABLE Price_Fact (
    RowID INT AUTO_INCREMENT PRIMARY KEY,
    VendorKey INT,
    FeedKey INT,
    SourceFeedKey INT,
    DateKey INT,
    ExchangeKey INT,
    PriceTypeKey INT,
    SecurityKey INT,
    IssueKey INT,
    Price DECIMAL(10,2),
    FOREIGN KEY (VendorKey) REFERENCES Vendor_Dim(VendorKey),
    FOREIGN KEY (FeedKey) REFERENCES Feed_Dim(FeedKey),
    FOREIGN KEY (SourceFeedKey) REFERENCES SourceFeed_Dim(SourceFeedKey),
    FOREIGN KEY (DateKey) REFERENCES Date_Dim(DateKey),
    FOREIGN KEY (ExchangeKey) REFERENCES Exchange_Dim(ExchangeKey),
    FOREIGN KEY (PriceTypeKey) REFERENCES PriceType_Dim(PriceTypeKey),
    FOREIGN KEY (SecurityKey) REFERENCES Security_Dim(SecurityKey),
    FOREIGN KEY (IssueKey) REFERENCES Issue_Dim(IssueKey)
);