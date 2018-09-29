<style scoped>
.layout {
  /* border: 1px solid #d7dde4; */
  background: #f5f7f9;
  position: relative;
  height: 100%;
}
.layout-breadcrumb {
  padding: 10px 15px 0;
  height: 3%;
}
.layout-content {
  height: 90%;
  margin: 0 15px;
  overflow: hidden;
  border-radius: 4px;
  overflow: auto;
}
.layout-content-main {
  padding: 10px;
}
.layout-copy {
  text-align: center;
  padding: 10px 0 20px;
  color: #9ea7b4;
  height: 4%;
}
.layout-menu-left {
  background: #464c5b;
}
.layout-header {
  height: 6%;
  background: #fff;
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.1);
}
.layout-logo-left {
  width: 90%;
  height: 30px;
  background: #5b6270;
  border-radius: 3px;
  margin: 15px auto;
}
</style>
<template>
    <div class="layout">
        <Row type="flex" style="height:100%">
            <i-Col span="4" class="layout-menu-left">
                <Menu active-name="" theme="dark" width="auto" :open-names="['1']">
                    <!-- <div class="layout-logo-left"></div> -->
                    <Submenu name="1">
                        <template slot="title">
                            <Icon type="ios-navigate"></Icon>
                            Item 1
                        </template>
                        <Menu-Item name="1-1">Option 1</Menu-Item>
                        <Menu-Item name="1-2">Option 2</Menu-Item>
                        <Menu-Item name="1-3">Option 3</Menu-Item>
                    </Submenu>
                    <Submenu name="2">
                        <template slot="title">
                            <Icon type="ios-keypad"></Icon>
                            Item 2
                        </template>
                        <Menu-Item name="2-1">Option 1</Menu-Item>
                        <Menu-Item name="2-2">Option 2</Menu-Item>
                    </Submenu>
                    <Submenu name="3">
                        <template slot="title">
                            <Icon type="ios-analytics"></Icon>
                            Item 3
                        </template>
                        <Menu-Item name="3-1">Option 1</Menu-Item>
                        <Menu-Item name="3-2">Option 2</Menu-Item>
                    </Submenu>
                </Menu>
            </i-Col>
            <i-Col span="20">
                <div class="layout-header">
                    <div class="layout-breadcrumb">
                        <Row type="flex" justify="start" align="middle">
                            <i-Col span="23">
                                <Breadcrumb>
                                    <BreadcrumbItem href="#">Home</BreadcrumbItem>
                                    <BreadcrumbItem href="#">Projects</BreadcrumbItem>
                                    <BreadcrumbItem>iView</BreadcrumbItem>
                                </Breadcrumb>
                            </i-Col>
                            <i-Col span="1">
                                <User user-avator="https://secure.gravatar.com/avatar/7b0ddb1000821f84626faa2efa14b4f6?s=46&d=identicon" />
                            </i-Col>
                        </Row>
                    </div>
                </div>
                <div class="layout-content">
                    <div class="layout-content-main">
                        <Row :gutter="20">
                            <i-col span="24">
                                <Card shadow>
                                    <life-gdp style="height: 500px;" :value="barData" text="每周用户活跃量" />
                                </Card>
                            </i-col>
                        </Row>
                        <Row :gutter="20" style="margin-top: 20px;">
                            <i-col span="8">
                                <Card shadow>
                                    <chart-pie style="height: 300px;" :value="pieData" text="用户访问来源"></chart-pie>
                                </Card>
                            </i-col>
                            <i-col span="16">
                                <Card shadow>
                                    <chart-bar style="height: 300px;" :value="barData" text="每周用户活跃量" />
                                </Card>
                            </i-col>
                        </Row>
                    </div>
                </div>
                <div class="layout-copy">
                    2011-2016 &copy; TalkingData
                </div>
            </i-Col>
        </Row>
    </div>
</template>
<script>
import { ChartPie, ChartBar, LifeGdp } from './charts'
import User from './user'
export default {
  name: 'home',
  components: {
    ChartPie,
    ChartBar,
    LifeGdp,
    User
  },
  data () {
    return {
      pieData: [
        { value: 335, name: '直接访问' },
        { value: 310, name: '邮件营销' },
        { value: 234, name: '联盟广告' },
        { value: 135, name: '视频广告' },
        { value: 1548, name: '搜索引擎' }
      ],
      barData: {
        Mon: 13253,
        Tue: 34235,
        Wed: 26321,
        Thu: 12340,
        Fri: 24643,
        Sat: 1322,
        Sun: 1324
      }
    }
  }
}
</script>
