const { expressjwt: jwt } = require("express-jwt");
const jwks = require("jwks-rsa")

// JWT verification
const jwtCheck = jwt({
    secret: jwks.expressJwtSecret({
        cache: true,
        rateLimit: true,
        jwksRequestsPerMinute: 5,
        // env.JWKSURI
        jwksUri: `process.env.JWKSURI`,
    }),
    audience: "This is an unique identifier",
    issuer: `process.env.JWKS_ISSUER`,
    algorithms: ["RS256"],
}).unless({path:['/']});

module.exports = jwtCheck;

