# Smart Rehabilitation and Physiotherapy Assistance System

## Theme
MedTech

## Background / Context
Physical rehabilitation requires consistent, repetitive exercises. Patients frequently perform these incorrectly at home without supervision, leading to poor recovery or re-injury.

## Problem Description
Lack of real-time feedback during home physiotherapy makes it difficult for patients to know if they are performing exercises correctly. Access to continuous professional supervision is expensive and limited.

## Core Challenge
Build a system that can track patient movements during specific exercises, compare them against an ideal motion profile, and provide corrective feedback.

## Expected Solution
A wearable or camera-based prototype that monitors joint angles or movement paths, giving visual or auditory feedback when the exercise is performed correctly or incorrectly.

## Expected Features
- Essential: Real-time motion tracking of at least one joint/limb, feedback mechanism (e.g., LED, buzzer, screen), data logging.
- Optional: Companion app dashboard, progress tracking over time, gamification.

## Suggested Hardware
IMU sensors (MPU6050), ESP32/Arduino, flex sensors, simple web camera (for OpenCV based tracking).

## Expected Deliverables
Working prototype, demonstration of an exercise, source code, circuit/system diagram, testing results, and brief documentation.

## Constraints
Must be affordable, wearable/portable, and provide low latency feedback.

## Evaluation Criteria
Functionality, accuracy of tracking, usability, real-world impact.

## Safety and Ethics
This is a prototype and not a substitute for professional diagnosis or treatment. The device must not restrict blood flow or cause physical discomfort. Data privacy must be maintained.
