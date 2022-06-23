<template>
  <div class="tdesign-demo-item--layout">
      <t-layout>
        <t-header class="affix-base" >
          <t-affix
            ref="affix"
          >
          <t-head-menu class="divider-line" theme="light" value="item1" height="150px">
            <div>
              <img
                slot="logo"
                width="136"
                class="logo"
                src="../images/menu_logo_hover.png"
                alt="logo"
              >
            </div>
              <div class="operations">
                <t-tooltip placement="bottom" content="数据上图">
                  <t-button theme="default" shape="square" variant="text">
                    <img src="../images/cloud-upload.svg">
                  </t-button>
                </t-tooltip>
                <t-tooltip placement="bottom" content="结果导出">
                  <t-button theme="default" shape="square" variant="text">
                    <img src="../images/download.svg">
                  </t-button>
                </t-tooltip>
              </div>
          </t-head-menu>
        </t-affix>
        </t-header>
        <t-layout>
          <t-aside class="affix-base">
            <t-affix
            ref="affix"
            >
            <div class="tdesign-tree-demo">
              <t-form>
                <t-tabs
                  :value="value1"
                  size="medium"
                  @change="(newValue) => value1 = newValue"
                >
                  <t-tab-panel value="first" label="仓库目录">
                    <t-form-item label="多选" >
                      <t-switch v-model="checkable" />
                    </t-form-item>
                    <div class="tree-widget">
                    <t-tree 
                      ref="tree"
                      :data="items"
                      activable
                      transition
                      hover
                      :checkable="checkable"
                      @change="onChange"
                      @click="onClick"
                    />
                  </div>
                  </t-tab-panel>
                  <t-tab-panel value="second" label="书本目录">
                    <t-form-item label="多选" >
                      <t-switch v-model="checkable" />
                    </t-form-item>
                    <div class="tree-widget">
                    <t-tree 
                      ref="tree"
                      :data="regionOptions"
                      activable
                      transition
                      hover
                      :checkable="checkable"
                      @change="onChange"
                      @click="onClick"
                    />
                  </div>
                  </t-tab-panel>
                </t-tabs>
              </t-form>
            </div>
          </t-affix>
          </t-aside>
          <t-layout>
            <t-content>
              <div class="table-tree-container">
              <div class="list-tree-content">
                <t-form class="form-content" :data="formData">
                  <t-form-item label="位置: " name="region">
                    <t-cascader class="t-demo-cascader" 
                    :keys="{ label: 'name', 
                    value: 'name', children: 'districts' }"
                    :options="options" v-model="value" clearable placeholder='请选择区域' @change="onChange"></t-cascader>
                    </t-cascader>
                  </t-form-item>
                  <t-form-item label="范围: " name="range">
                    <t-radio-group label= "选择: " 
                    default-value="1"
                    v-model="formData.range">
                      <t-radio value="1">30km</t-radio>
                      <t-radio value="2">60km</t-radio>
                      <t-radio value="3">120km</t-radio>
                    </t-radio-group>
                  </t-form-item>
                  <t-form-item label="更多: " name="more_options">
                    <t-checkbox-group 
                    v-model="formData.more_options"
                    :options="moreOptions">
                    </t-checkbox-group>
                  </t-form-item>
                </t-form>
                <t-table
                  rowKey="index"
                  :data="list"
                  :columns="columns"
                  :stripe="stripe"
                  :hover="hover"
                  :size="size"
                  :table-layout="tableLayout ? 'auto' : 'fixed'"
                  :pagination="pagination"
                >
                </t-table>
                </div>
              </div>
            </t-content>
            <t-footer>Copyright @ 2021-{{new Date().getFullYear()}} BlackAnt. All Rights Reserved
            </t-footer>

          </t-layout>
        </t-layout>
      </t-layout>
  </div>
</template>
<script type="text/javascript">
import constants from './constants.js'
import axios from './axios.min.js'
import ref from 'vue'
import $ from 'jquery'
import geodata from './geoinfo-all.json'
const INITIAL_DATA = {
  region: '2.2',
  range: '2',
  more_options: [],
};

export default {
  data() {
    return {
      check: [],
      list: [],
      size: 'medium',
      tableLayout: true,
      stripe: true,
      bordered: true,
      hover: false,
      columns: [
        {
          width: '100',
          // colKey: 'index',
          colKey: 'id',
          title: '序号',
          // 对齐方式
          align: 'center',
          // 设置列类名
          className: 'custom-column-class-name',
          // 设置列属性
          attrs: {
            'data-id': 'first-column',
          },
        },
        {
          width: 100,
          // colKey: 'no',
          colKey: 'id',
          title: '平台',
        },
        {
          // colKey: 'status',
          colKey: 'name',
          title: '类型',
        },
        {
          // colKey: 'contractType',
          colKey: 'birth_date',
          title: '默认值',
        },
        {
          // colKey: 'paymentType',
          colKey: 'id',
          title: '是否必传',
        },
        {
          colKey: 'name',
          title: '详情信息',
          width: 200,
          /**
           * 1.内容超出时，是否显示省略号。值为 true，则浮层默认显示单元格内容；
           * 2.值类型为 Function 则自定义浮层显示内容；
           * 3.值类型为 Object，则自动透传属性到 Popup 组件。
           */
          ellipsis: true,
        },
      ],/** 非受控用法：与分页组件对齐 */
      pagination: {
        defaultCurrent: 1,
        defaultPageSize: 6
      },
      checkable: false,
      formData: { ...INITIAL_DATA },
      /* multichoices */
      moreOptions: [
        {
          label: "开发能力",
          value: "1",
        },
        {
          label: "车辆检测现状",
          value: "2",
        },
      ],
      /* tree data */
      items: [],
      value1: 'second',
      /* location options */
      options: [],
      value: '',
      regionOptions: [],
    };
  },
  watch: {
    'formData.region': function () {
      console.log(this.formData.region)
    },
    'formData.range': function () {
      console.log(this.formData.range)
    },
    'formData.more_options': function () {
      this.fetchData();
      console.log(this.formData.more_options);
    },
  },
  mounted() {
    this.regionOptions = constants.TREE_DATA;
    this.items = constants.TREE_DATA_AFF;
    this.options = geodata;
  },
  methods: {
    async fetchData(checked) {
      var tmps = this.formData.more_options;
      if (checked) // has data
        this.check = checked;
      var tmp = this.check;
      var suffix = '';
      if (tmps.length == 1) {
        if (tmps[0] == 1)
          suffix = '/checked_more_1/';
        if (tmps[0] == 2)
          suffix = '/checked_more_2/';
      } 
      else if (tmps.length == 2) 
        suffix = '/checked_more_12/';
      else
        suffix = '/checked/';
      
      axios.get(
        // 'http://localhost:5000' + suffix + tmp
        'http://172.16.16.3:5000' + suffix + tmp
        // 'http://172.16.16.3:5000/todos'
      )
        .then(response => {
          console.log('here: ', response.data);
          this.list = response.data;
          this.pagination = {
            ... this.pagination,
            total: this.list.length
          };
        })
        .catch(function (error) { // 请求失败处理
          console.log(error);
      });
  },
    onClick(context) {
      // console.info('onClick:', context.node.data.value); // current node
      this.fetchData(context.node.data.value);
      // call the params
    },
    onChange(checked, context) { // checked 
      this.fetchData(checked);
      // console.info('data:', constants.TREE_DATA); // load data file
    },
    onChange(val, context) {
      if (val) // has data
        console.log(context.node.data.center);
      // console.log('path: ', context.node.getPath());
    },
    load(node) {
      return new Promise((resolve) => {
        setTimeout(() => {
          let nodes = [];
          nodes = [
              {
                label: 'nanj',
                children: node.level < 1, // if has children
              },
              {
                label: 'shanghai',
                children: node.level < 2,
              },
            ];
          resolve(nodes);
          console.info('node:', node);
        }, 300);
      });
    },
  },
};   

</script>

<style>
.operations {
  position: absolute;
  right: 10px;
}
.divider-line {
  box-shadow: inset 0 -1px 0 #e7e7e7;
}
.tdesign-tree-demo .t-tree {
  max-height: 500px;
  margin-bottom: 10px;
  padding: 5px;
  overflow: auto;
  /*bottom: 100px;*/
}
.tdesign-tree-demo .title{
  margin-bottom: 10px;
}
.tdesign-tree-demo .tips{
  margin-bottom: 10px;
}
.tdesign-tree-demo .operations{
  margin-top: 10px;
  margin-bottom: 10px;
  padding: 5px;
  box-shadow: inset 0 -1px 0 #e7e7e7;
  border:1px solid red;
  outline:green dotted thick;
}
.tdesign-tree-demo .t-form__item {
  margin-bottom: 0px;
}
.tdesign-tree-demo .t-button{
  margin: 0 10px 10px 0;
}

.table-tree-container {
  /*background-color: @bg-color-container;*/
  background-color: @background-color;
  border-radius: @border-radius;
}

.list-tree-content {
  border-left: 1px solid @border-level-1-color;
  /*overflow: auto;*/
  padding: 20px;
}

.form-content {
  background-color: #ffffff;
  padding: 20px;
}
</style>



