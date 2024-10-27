# Keynote for: 


# Key variables include:
- id: borrower id
- time: time stamp of observation
- orig_time: time stamp for origination
- first_time: time stamp for first observation
- mat_time: time stamp for maturity
- res_time: time stamp for resolution
- balance_time: outstanding balance at observation time
- LTV_time: loan to value ratio at observation time, in %
- interest_rate_time: interest rate at observation time, in %
- rate_time: risk-free rate
- hpi_time: house price index at observation time, base year=100
- gdp_time: GDP growth at observation time, in %
- uer_time: unemployment rate at observation time, in %
- REtype_CO_orig_time: real estate type condominium: 1, otherwise: 0
- REtype_PU_orig_time: real estate type planned urban developments: 1, otherwise: 0
- REtype_SF_orig_time: single family home: 1, otherwise: 0
- investor_orig_time: investor borrower: 1, otherwise: 0
- balance_orig_time: outstanding balance at origination time
- FICO_orig_time: FICO score at origination time, in %
- LTV_orig_time: loan to value ratio at origination time, in %
- Interest_Rate_orig_time: interest rate at origination time, in %
- state_orig_time: US state in which the property is located
- hpi_orig_time: house price index at observation time, base year=100
- default_time: default observation at observation time
- payoff_time: payoff observation at observation time
- status_time: default (1), payoff (2) and non-default/non-payoff (0) observation at observation time
- lgd_time: LGD assuming no discounting of cash flows
- recovery_res: sum of all cash flows received during resolution period