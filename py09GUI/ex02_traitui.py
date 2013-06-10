#!/usr/bin/env python

'''Ex02, TraitsUI and chaco practise

In this exercise, we will practise how to use traitsui and simple chaco
generally, follow the instructions, change some code and run it to see the 
changes
'''


# Major library imports
from numpy import linspace, sin, ceil

# Enthought library imports
from enable.api import Component, ComponentEditor
from traits.api import HasTraits, Instance, Int
from traitsui.api import Item, Group, HGroup, View, VGroup, Tabbed

# Chaco imports
from chaco.api import ScatterPlot, DataView, LinePlot
from chaco.tools.api import PanTool, ZoomTool
from chaco.function_data_source import FunctionDataSource


class PlotExample(HasTraits):
    plot = Instance(Component)
    numpoints = Int(500)

    traits_view = View(
        Group(
            # here create a chaco component
            Item('plot', editor=ComponentEditor(), show_label=False),
            # FIXME: change HGroup to Tabbed to make panels shown in tabs
            HGroup(
                # FIXME: change HGroup to VGroup to arrange panels vertically
                HGroup(
                    Item('object.plot.x_mapper.range.low_setting', label='Low'),
                    Item('object.plot.x_mapper.range.high_setting', label='High'),
                    label='X', show_border=True
                ),
                HGroup(
                    # FIXME: change to 'object.plot.y_mapper.range.low' to see
                    # the difference
                    Item('object.plot.y_mapper.range.low_setting', label='Low'),
                    # FIXME: add key: style='custom' to see the difference
                    Item('object.plot.y_mapper.range.high_setting', label='High'),
                    label='Y', show_border=True
                ),
            ),
            #FIXME: change orientation to 'horizontal' to arange panels horizontally
            orientation = "vertical"), resizable=True, title="Function Plot",
            width=900, height=600
        )

    def xfunc(self, low, high):
        dx = (high - low) / self.numpoints
        real_low = ceil(low/dx) * dx
        real_high = ceil(high/dx) * dx
        return linspace(real_low, real_high, self.numpoints)

    def yfunc(self, low, high):
        x = self.xfunc(low, high)
        return sin(1.0/x)

    def _plot_default(self):
        container = DataView()

        xds = FunctionDataSource(func = self.xfunc)
        yds = FunctionDataSource(func = self.yfunc)

        xmapper = container.x_mapper
        ymapper = container.y_mapper

        xds.data_range = xmapper.range
        yds.data_range = xmapper.range

        xmapper.range.set_bounds(-5, 10)
        ymapper.range.set_bounds(-1, 1.2)
        
        #FIXME: change color, marker, marker_size to see the difference
        plot = ScatterPlot(index = xds, value = yds, index_mapper = xmapper,
                           value_mapper = ymapper,
                           color = "green",
                           marker = "circle",
                           marker_size = 3,
                           line_width = 0)

        plot2 = LinePlot(index = xds, value = yds, index_mapper = xmapper,
                        value_mapper = ymapper,
                        color = "lightgray")

        container.add(plot2, plot)
        #FIXME: uncomment following two lines to see the difference
        #plot.tools.append(PanTool(plot, constrain_direction="x", constrain=True))
        #plot.tools.append(ZoomTool(plot, axis="index", tool_mode="range"))

        return container


demo = PlotExample()

if __name__ == "__main__":
    demo.configure_traits()