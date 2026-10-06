# AeroPulse — Airline Operations & Passenger Analytics

An interactive Power BI analytics project designed to analyze airline operations, passenger activity, flight performance, delays, load factor, and revenue.

## Project Overview

AeroPulse analyzes 100,000 airline flight records covering the period from January 2025 to June 2026.

The project combines Python-based data generation and quality validation with Power BI dashboarding to provide an executive view of airline operational and passenger performance.

## Business Objectives

- Monitor overall flight operations and passenger volume
- Analyze on-time and delayed flight performance
- Identify major flight delay reasons
- Compare airline load factor performance
- Analyze passenger distribution across regions
- Compare airline revenue performance
- Understand relationships between flight duration and delays
- Provide interactive filtering for Year, Region, and Airline

## Dataset

- Records: 100,000 flights
- Time Period: January 2025 – June 2026
- Number of Columns: 25
- Airlines: 5
- Flight Statuses: On Time, Delayed, Cancelled
- Regions: Domestic and International

### Key Dataset Fields

- Flight_ID
- Flight_Date
- Airline
- Origin
- Destination
- Region
- Aircraft_Type
- Distance_KM
- Flight_Hours
- Capacity
- Passengers
- Load_Factor
- Delay_Minutes
- Delay_Reason
- Flight_Status
- On_Time
- Cancelled
- Ticket_Price
- Revenue
- Operating_Cost
- Profit
- Booking_Channel
- Customer_Type
- Baggage_Issues
- Satisfaction_Score

## Key KPIs

The dashboard tracks:

- Total Flights
- Total Passengers
- On-Time Performance
- Average Load Factor
- Total Revenue
- Flight Status Distribution
- Average Delay
- Airline Performance

## Power BI Dashboard

The executive dashboard provides:

- Flight Status Distribution
- Monthly Flight Trends
- Flight Delay Reasons
- Load Factor by Airline
- Flight Duration vs Delay
- On-Time vs Delayed Flights by Month
- Passenger Distribution by Region
- Revenue by Airline

Interactive slicers allow analysis by:

- Year
- Region
- Airline

## Data Quality

The dataset was validated using Python before dashboard development.

Validation included:

- Row count verification
- Column validation
- Missing-value checks
- Duplicate Flight_ID checks
- Date-range validation
- Flight-status distribution
- Airline distribution

## Project Workflow

```text
Data Generation
      ↓
Data Quality Validation
      ↓
Data Preparation
      ↓
Power BI Data Modeling
      ↓
DAX Measures
      ↓
Interactive Dashboard
      ↓
Business Insights