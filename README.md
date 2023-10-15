# 一套酒店空调管理系统

![Github](https://img.shields.io/github/license/FlyingASea/My-SE-HomeWork)

![GitHub top language](https://img.shields.io/github/languages/top/FlyingASea/My-SE-HomeWork)
![GitHub file size](https://img.shields.io/github/languages/code-size/FlyingASea/My-SE-HomeWork)

![GitHub Repo stars](https://img.shields.io/github/stars/FlyingASea/My-SE-HomeWork?style=social)
![GitHub forks](https://img.shields.io/github/forks/FlyingASea/My-SE-HomeWork?style=social)

## 项目介绍

本项目是一个用于管理酒店业务的简单酒店管理系统，提供了下面一系列的功能：

- 使酒店管理员能够管理房间的空调、查询房间空调的状态等。
- 空调通过http通信的方式向服务器发送信息

## 功能特点

- 空调信息管理：管理员可以添加、编辑和删除客房空调信息
- 空调信息传递：空调在向服务器传送信息的时候采用http传递的方式
- 系统自动报表：在住户退房以后，空调管理系统后台能自动提供一份空调使用报表，报表中包括空调使用应缴纳的费用和空调使用情况，以帮助酒店工作人员减少计算工作量
- 完善的系统报错：在空调或者服务器出现问题之后，拥有完整完善的系统报错提示

## 技术介绍

该项目使用以下的技术来进行开发：

- 前端：利用figma来设计网站，vue框架来进行网站的开发
- 后端：采用了python和flask框架
- 数据库：使用了sqlite数据库

## 快速开始

在使用该项目之前，请先确保电脑上有python环境，最好版本为3.9.13

作者电脑上的环境配置为python3.9.13

### 环境要求
- python 3.6-3.10版本
- Flask 
- sqlite

### 安装和设置
